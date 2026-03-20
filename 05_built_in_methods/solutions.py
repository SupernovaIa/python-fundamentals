# 05 — Built-in Methods
# Solutions

# ============================================================
# Exercise 1 — String cleaning and validation
# ============================================================

raw_email = "  USER@EXAMPLE.COM  "
raw_name = "  javi garcía  "
raw_age = "  29  "

email = raw_email.strip().lower()
name = raw_name.strip().title()
age_str = raw_age.strip()
age = int(age_str) if age_str.isdigit() else None

print(email)    # user@example.com
print(name)     # Javi García
print(age)      # 29


# ============================================================
# Exercise 2 — String searching
# ============================================================

text = "Becoming a Python engineer. Python engineers are in high demand."

print(text.lower().count("python"))          # 2
print(text.lower().find("engineer"))         # 18
print(text.startswith("Becoming"))           # True
print(text.endswith((".pdf", ".txt", "engineer")))  # True  (ends with "engineer")


# ============================================================
# Exercise 3 — Split and join
# ============================================================

csv_line = "name ,  age , city ,  role  , department"

fields = [f.strip() for f in csv_line.split(",")]
clean_csv = ",".join(fields)

print(clean_csv)           # name,age,city,role,department
print(len(fields))         # 5


# ============================================================
# Exercise 4 — f-string formatting
# ============================================================

name = "Ada Lovelace"
price = 9875432.5
rate = 0.7348
progress = 0.5

print(f"{name:>20}")                                    # right-aligned in 20 chars
print(f"{price:,.2f}")                                  # 9,875,432.50
print(f"{rate:.1%}")                                    # 73.5%

filled = int(progress * 10)
bar = "=" * filled + " " * (10 - filled)
print(f"Progress: [{bar}] {progress:.0%}")              # Progress: [=====     ] 50%


# ============================================================
# Exercise 5 — Sorting with key
# ============================================================

products = [
    {"name": "Laptop", "price": 999.99, "stock": 5},
    {"name": "monitor", "price": 349.50, "stock": 12},
    {"name": "Keyboard", "price": 79.99, "stock": 30},
    {"name": "mouse", "price": 29.99, "stock": 8},
    {"name": "Headset", "price": 149.99, "stock": 20},
]

by_price = sorted(products, key=lambda p: p["price"])
by_name = sorted(products, key=lambda p: p["name"].lower())
by_stock_desc = sorted(products, key=lambda p: p["stock"], reverse=True)

print("By price:", [p["name"] for p in by_price])
print("By name:", [p["name"] for p in by_name])
print("By stock (desc):", [p["name"] for p in by_stock_desc])


# ============================================================
# Exercise 6 — setdefault
# ============================================================

logs = [
    ("INFO", "Server started"),
    ("ERROR", "Connection failed"),
    ("INFO", "Request received"),
    ("WARNING", "High memory usage"),
    ("ERROR", "Timeout exceeded"),
    ("INFO", "Request completed"),
]

grouped: dict[str, list[str]] = {}
for level, message in logs:
    grouped.setdefault(level, []).append(message)

for level, messages in grouped.items():
    print(f"{level}: {messages}")


# ============================================================
# Exercise 7 — fromkeys and common mistakes
# ============================================================

# Part A: create a dict with default value 0
metrics = ["clicks", "impressions", "conversions", "revenue"]
metric_dict = dict.fromkeys(metrics, 0)
print(metric_dict)

# Part B: fix the shared-list bug
# broken = dict.fromkeys(["a", "b", "c"], [])  ← all keys share ONE list

# Fix: use a dict comprehension so each key gets its own list
fixed = {k: [] for k in ["a", "b", "c"]}
fixed["a"].append(1)
print(fixed)   # {'a': [1], 'b': [], 'c': []}


# ============================================================
# Exercise 8 — In-place set operations
# ============================================================

a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}

# Union in-place
a |= b
print(a)                   # {1, 2, 3, 4, 5, 6, 7, 8}

# Reset
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}

# Intersection in-place
a &= b
print(a)                   # {4, 5}

# Reset
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}

# Difference in-place
a -= b
print(a)                   # {1, 2, 3}
