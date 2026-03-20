# 06 — Control Flow
# Solutions

# ============================================================
# Exercise 1 — Conditionals
# ============================================================

for score in [95, 83, 71, 65, 42]:
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "Fail"

    status = "passing" if score >= 60 else "failing"
    print(f"{score} → {grade} ({status})")


# ============================================================
# Exercise 2 — for loop with range
# ============================================================

number = 7
total = 0

for i in range(1, 13):
    result = number * i
    total += result
    print(f"{number} × {i} = {result}")

print(f"Sum of all results: {total}")


# ============================================================
# Exercise 3 — enumerate and zip
# ============================================================

students = ["Ana", "Juan", "María", "Carlos", "Beatriz"]
grades = [87, 92, 78, 95, 83]

# enumerate (1-indexed)
for i, student in enumerate(students, start=1):
    print(f"{i}. {student}")

print()

# zip
for student, grade in zip(students, grades):
    print(f"{student}: {grade}")

print()

# zip + enumerate
for i, (student, grade) in enumerate(zip(students, grades), start=1):
    print(f"{i}. {student} — {grade}")


# ============================================================
# Exercise 4 — while loop
# ============================================================

correct_password = "ai2026"
guesses = ["wrong1", "wrong2", "ai2026"]
max_attempts = 3
attempts = 0

while attempts < max_attempts:
    guess = guesses[attempts]
    attempts += 1
    if guess == correct_password:
        print("Access granted")
        break
    remaining = max_attempts - attempts
    if remaining > 0:
        print(f"Wrong password. {remaining} attempt(s) remaining.")
else:
    print("Account locked")


# ============================================================
# Exercise 5 — break, continue, else
# ============================================================

# Part A: find first number divisible by both 3 and 7
numbers = [4, 9, 14, 21, 35, 42, 63, 77]

for n in numbers:
    if n % 3 == 0 and n % 7 == 0:
        print(f"Found: {n}")
        break
else:
    print("Not found")

# Part B: skip negatives, sum valid transactions
transactions = [120, -30, 450, -15, 200, 80, -5, 310]
total = 0

for t in transactions:
    if t < 0:
        continue
    print(f"Valid: {t}")
    total += t

print(f"Total: {total}")


# ============================================================
# Exercise 6 — zip advanced
# ============================================================

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Transpose: swap rows and columns
transposed = list(zip(*matrix))
for row in transposed:
    print(row)

# Column sums
for col_index, col in enumerate(zip(*matrix)):
    print(f"Column {col_index} sum: {sum(col)}")


# ============================================================
# Exercise 7 — List comprehensions
# ============================================================

words = ["ai", "python", "llm", "agent", "rag", "embedding"]
nested = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]

# Squares of odd numbers from 1 to 20
odd_squares = [n ** 2 for n in range(1, 21) if n % 2 != 0]
print(odd_squares)

# Words longer than 4 chars in uppercase
long_upper = [w.upper() for w in words if len(w) > 4]
print(long_upper)

# Flatten nested list
flat = [item for sublist in nested for item in sublist]
print(flat)


# ============================================================
# Exercise 8 — Dict and set comprehensions
# ============================================================

prices = {
    "keyboard": 79.99,
    "mouse": 29.99,
    "monitor": 349.50,
    "headset": 149.99,
    "webcam": 89.99,
    "usb hub": 24.99,
}

# Dict: items under £100, prices rounded
cheap = {item: round(price) for item, price in prices.items() if price < 100}
print(cheap)

# Set of unique price ranges
def price_range(p: float) -> str:
    if p < 50:
        return "budget"
    elif p <= 200:
        return "mid"
    return "premium"

ranges = {price_range(p) for p in prices.values()}
print(ranges)


# ============================================================
# Exercise 9 — Generator expressions
# ============================================================

# Generator expression — computes on demand, no list in memory
total_gen = sum(n ** 2 for n in range(1, 1_000_001) if n % 2 == 0)

# List comprehension — builds the whole list first
total_list = sum([n ** 2 for n in range(1, 1_000_001) if n % 2 == 0])

print(total_gen == total_list)   # True
print(total_gen)
