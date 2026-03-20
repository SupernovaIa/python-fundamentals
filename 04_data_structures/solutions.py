# 04 — Data Structures
# Solutions

# ============================================================
# Exercise 1 — Lists
# ============================================================

topics = ["python", "llms", "web", "agents", "rag"]

print(topics[0], topics[-1])        # python rag
print(topics[1:4])                  # ['llms', 'web', 'agents']
topics.append("mlops")
topics.insert(2, "databases")
topics.remove("web")
print(topics)
print(len(topics))


# ============================================================
# Exercise 2 — Copying lists
# ============================================================

original = [1, 2, 3, 4, 5]
copy = original.copy()              # or: copy = original[:]  or  list(original)
copy[0] = 999
print(original)   # [1, 2, 3, 4, 5]  ← unchanged
print(copy)       # [999, 2, 3, 4, 5]


# ============================================================
# Exercise 3 — Tuples
# ============================================================

user = ("Javi", 29, "Madrid", "AI Engineer")

name, age, city, role = user
print(f"Name: {name}")
print(f"Age:  {age}")
print(f"City: {city}")
print(f"Role: {role}")

# Trying to change a tuple raises TypeError:
try:
    user[1] = 30   # type: ignore[index]
except TypeError as e:
    print(f"Cannot modify tuple: {e}")

# Convert to list, change age, convert back:
user_list = list(user)
user_list[1] = 30
user = tuple(user_list)
print(user)   # ('Javi', 30, 'Madrid', 'AI Engineer')


# ============================================================
# Exercise 4 — Extended unpacking
# ============================================================

numbers = (10, 20, 30, 40, 50)
first, *middle, last = numbers
print(f"first:  {first}")    # 10
print(f"middle: {middle}")   # [20, 30, 40]
print(f"last:   {last}")     # 50


# ============================================================
# Exercise 5 — Dictionaries
# ============================================================

person = {
    "name": "Javi",
    "age": 29,
    "city": "Madrid",
    "skills": ["Python", "ML", "LLMs"],
}

print(person["name"], person["city"])

person["role"] = "AI Engineer"
person["age"] += 1
removed_city = person.pop("city")
print(f"Removed city: {removed_city}")
print("email" in person)   # False


# ============================================================
# Exercise 6 — Iterating dictionaries
# ============================================================

inventory = {"laptops": 15, "monitors": 8, "keyboards": 42, "mice": 37, "headsets": 11}

for product, qty in inventory.items():
    print(f"{product}: {qty} units")

total = sum(inventory.values())
print(f"Total units: {total}")


# ============================================================
# Exercise 7 — Sets
# ============================================================

team_a = ["python", "sql", "r", "scala", "java"]
team_b = ["python", "sql", "go", "rust", "java"]

set_a = set(team_a)
set_b = set(team_b)

print("Both teams:", set_a & set_b)           # {'python', 'sql', 'java'}
print("Only team A:", set_a - set_b)           # {'r', 'scala'}
print("Only team B:", set_b - set_a)           # {'go', 'rust'}
print("All unique:", set_a | set_b)
print("Subset check:", {"python", "sql"} <= set_a)   # True


# ============================================================
# Exercise 8 — Choosing the right structure
# ============================================================

# Scenario A: (latitude, longitude) of a location
# → tuple: fixed-size, ordered, immutable; values won't change
location = (40.4168, -3.7038)

# Scenario B: track users who visited a page (no duplicates)
# → set: O(1) lookup, enforces uniqueness automatically
visitors = {"user_01", "user_02", "user_03"}

# Scenario C: shopping cart with item names and quantities
# → dict: key-value pairs; look up by item name in O(1)
cart = {"laptop": 1, "mouse": 2, "keyboard": 1}

# Scenario D: sequence of daily temperatures for analysis
# → list: ordered, mutable, supports indexing and slicing
temperatures = [18.5, 21.0, 19.3, 22.7, 20.1]
