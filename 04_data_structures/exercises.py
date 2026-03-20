# 04 — Data Structures
# Exercises

# ============================================================
# Exercise 1 — Lists
# Given the list below:
# - Print the first and last element
# - Print the three middle elements using slicing
# - Add "mlops" at the end
# - Insert "databases" at index 2
# - Remove "web" by value
# - Print the final list and its length
#
# topics = ["python", "llms", "web", "agents", "rag"]
# ============================================================

topics = ["python", "llms", "web", "agents", "rag"]

# Your code here


# ============================================================
# Exercise 2 — Copying lists
# Fix the code below so that modifying copy does not
# affect original.
#
# original = [1, 2, 3, 4, 5]
# copy = original
# copy[0] = 999
# print(original)  # should still be [1, 2, 3, 4, 5]
# ============================================================

original = [1, 2, 3, 4, 5]

# Your code here


# ============================================================
# Exercise 3 — Tuples
# Given the tuple below:
# - Unpack it into four variables: name, age, city, role
# - Print each variable with a label
# - Try to change the age — what happens?
# - Convert it to a list, change the age to 30,
#   and convert it back to a tuple
#
# user = ("Javi", 29, "Madrid", "AI Engineer")
# ============================================================

user = ("Javi", 29, "Madrid", "AI Engineer")

# Your code here


# ============================================================
# Exercise 4 — Extended unpacking
# Unpack the following tuple so that:
# - first gets the first element
# - middle gets all elements except first and last
# - last gets the last element
# Print all three.
#
# numbers = (10, 20, 30, 40, 50)
# ============================================================

numbers = (10, 20, 30, 40, 50)

# Your code here


# ============================================================
# Exercise 5 — Dictionaries
# Create a dictionary representing a person with at least
# these keys: name, age, city, skills (a list).
# Then:
# - Print the person's name and city
# - Add a new key "role" with any value
# - Update the age by 1
# - Remove the city key using pop() and print the removed value
# - Check if "email" exists in the dictionary
# ============================================================

# Your code here


# ============================================================
# Exercise 6 — Iterating dictionaries
# Given the inventory below, print each product and its
# quantity in the format: "product: X units"
# Then print the total number of units across all products.
#
# inventory = {
#     "laptops": 15,
#     "monitors": 8,
#     "keyboards": 42,
#     "mice": 37,
#     "headsets": 11
# }
# ============================================================

inventory = {"laptops": 15, "monitors": 8, "keyboards": 42, "mice": 37, "headsets": 11}

# Your code here


# ============================================================
# Exercise 7 — Sets
# Given the two lists below:
# - Convert both to sets
# - Find the languages that appear in both lists
# - Find the languages only in team_a
# - Find the languages only in team_b
# - Find all unique languages across both teams
# - Check if {"python", "sql"} is a subset of team_a
#
# team_a = ["python", "sql", "r", "scala", "java"]
# team_b = ["python", "sql", "go", "rust", "java"]
# ============================================================

team_a = ["python", "sql", "r", "scala", "java"]
team_b = ["python", "sql", "go", "rust", "java"]

# Your code here


# ============================================================
# Exercise 8 — Choosing the right structure
# For each scenario below, choose the most appropriate
# data structure and explain why in a comment.
# Then create an example of each.
#
# Scenario A: store the (latitude, longitude) of a location
# Scenario B: track which users have visited a page (no duplicates)
# Scenario C: store a shopping cart with item names and quantities
# Scenario D: store a sequence of daily temperatures that will be analysed
# ============================================================

# Your code here
