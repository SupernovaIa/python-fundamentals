# 06 — Control Flow
# Exercises

# ============================================================
# Exercise 1 — Conditionals
# Given a score between 0 and 100, print the grade:
# - 90-100: "A"
# - 80-89:  "B"
# - 70-79:  "C"
# - 60-69:  "D"
# - below 60: "Fail"
# Also print whether the score is passing (>= 60) or failing
# using a ternary operator.
#
# Test with: 95, 83, 71, 65, 42
# ============================================================

score = 95

# Your code here


# ============================================================
# Exercise 2 — for loop with range
# Print a multiplication table for a given number.
# Format each line as: "7 × 3 = 21"
# Then print the sum of all results.
#
# number = 7
# ============================================================

number = 7

# Your code here


# ============================================================
# Exercise 3 — enumerate and zip
# Given the two lists below:
# - Use enumerate to print each student with their position
#   (1-indexed): "1. Ana"
# - Use zip to pair each student with their grade and print:
#   "Ana: 87"
# - Use zip and enumerate together to print:
#   "1. Ana — 87"
#
# students = ["Ana", "Juan", "María", "Carlos", "Beatriz"]
# grades = [87, 92, 78, 95, 83]
# ============================================================

students = ["Ana", "Juan", "María", "Carlos", "Beatriz"]
grades = [87, 92, 78, 95, 83]

# Your code here


# ============================================================
# Exercise 4 — while loop
# Simulate a simple login system:
# - The user has 3 attempts to enter the correct password
# - After each wrong attempt, print how many attempts remain
# - If successful, print "Access granted"
# - If all attempts are used, print "Account locked"
# Use a hardcoded password for testing (no actual input needed —
# simulate attempts with a list of guesses).
#
# correct_password = "ai2026"
# guesses = ["wrong1", "wrong2", "ai2026"]
# ============================================================

correct_password = "ai2026"
guesses = ["wrong1", "wrong2", "ai2026"]

# Your code here


# ============================================================
# Exercise 5 — break, continue, else
# Part A: Given the list of numbers below, find the first
# number divisible by both 3 and 7. Print it and stop.
# If none exists, print "Not found".
#
# numbers = [4, 9, 14, 21, 35, 42, 63, 77]
#
# Part B: Given the list of transactions below, skip any
# negative values and print only the valid ones.
# At the end, print the total of valid transactions.
#
# transactions = [120, -30, 450, -15, 200, 80, -5, 310]
# ============================================================

numbers = [4, 9, 14, 21, 35, 42, 63, 77]
transactions = [120, -30, 450, -15, 200, 80, -5, 310]

# Your code here


# ============================================================
# Exercise 6 — zip advanced
# Given the matrix below, use zip(*matrix) to transpose it
# (swap rows and columns) and print the result row by row.
# Then compute the sum of each column in the original matrix.
#
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# ============================================================

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Your code here


# ============================================================
# Exercise 7 — List comprehensions
# Using list comprehensions (no traditional loops):
# - Create a list of squares of odd numbers from 1 to 20
# - From the words list, keep only words longer than 4 chars
#   and convert them to uppercase
# - Flatten the nested list into a single list
#
# words = ["ai", "python", "llm", "agent", "rag", "embedding"]
# nested = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
# ============================================================

words = ["ai", "python", "llm", "agent", "rag", "embedding"]
nested = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]

# Your code here


# ============================================================
# Exercise 8 — Dict and set comprehensions
# - From the prices dict, create a new dict with only items
#   that cost less than 100, with prices rounded to 0 decimals
# - From the same dict, create a set of unique price ranges:
#   "budget" if price < 50, "mid" if 50-200, "premium" if > 200
#
# prices = {
#     "keyboard": 79.99,
#     "mouse": 29.99,
#     "monitor": 349.50,
#     "headset": 149.99,
#     "webcam": 89.99,
#     "usb hub": 24.99,
# }
# ============================================================

prices = {
    "keyboard": 79.99,
    "mouse": 29.99,
    "monitor": 349.50,
    "headset": 149.99,
    "webcam": 89.99,
    "usb hub": 24.99,
}

# Your code here


# ============================================================
# Exercise 9 — Generator expressions
# Given a list of 1 million numbers (use range(1, 1_000_001)):
# - Compute the sum of squares of even numbers using a
#   generator expression (not a list comprehension)
# - Compute the same using a list comprehension
# - Both should give the same result
# (No need to measure time, just understand the difference
# in how memory is used)
# ============================================================

# Your code here
