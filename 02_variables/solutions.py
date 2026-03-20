# 02 — Variables
# Solutions

import math

# ============================================================
# Exercise 1
# ============================================================

name = "Javi"
age = 29
height = 1.75

print(name)
print(age)
print(height)


# ============================================================
# Exercise 2
# ============================================================

word = "engineer"

print(word[0])        # first character: 'e'
print(word[-1])       # last character: 'r'
print(word[:3])       # first three: 'eng'
print(word[::-1])     # reversed: 'reenigne'


# ============================================================
# Exercise 3
# ============================================================

first_name = "Ada"
last_name = "Lovelace"
full_name = first_name + " " + last_name

print(full_name)
print(len(full_name))


# ============================================================
# Exercise 4
# ============================================================

result = 0.1 + 0.2
print(result)                          # 0.30000000000000004
print(math.isclose(result, 0.3))       # True


# ============================================================
# Exercise 5
# ============================================================

# Predictions:
# bool(0)        → False
# bool(1)        → True
# bool("")       → False
# bool("hello")  → True
# bool([])       → False
# bool(None)     → False

print(bool(0))
print(bool(1))
print(bool(""))
print(bool("hello"))
print(bool([]))
print(bool(None))


# ============================================================
# Exercise 6
# ============================================================

value = None

if value is None:
    print("No value assigned yet")
else:
    print(value)


# ============================================================
# Exercise 7
# ============================================================

# Original (violates PEP 8):
# MyName="Javi"
# NumberOFItems=5
# PI_VALUE=3.14

my_name = "Javi"
number_of_items = 5
PI_VALUE = 3.14  # constants use UPPER_CASE
