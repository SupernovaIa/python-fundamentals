# 06 — Control Flow

So far, all the code we have written executes sequentially — line by line, top to bottom. Real programs need to be smarter: they must make decisions, repeat actions and respond to different situations dynamically.

Python organises control flow into four tools:
- **Conditionals** (`if`, `elif`, `else`) — make decisions based on conditions.
- **Loops** (`for`, `while`) — repeat code in a controlled way.
- **Loop control** (`break`, `continue`, `pass`) — fine-tune how loops behave.
- **Comprehensions** — a concise, Pythonic way to build collections.

---

## Conditionals

### if

The most basic decision structure. If the condition is `True`, the indented block runs. If not, Python skips it.

```python
age = 20

if age >= 18:
    print("Adult")
```

> **Indentation is not optional in Python.** It defines which code belongs to which block. Use 4 spaces consistently.

### else

Runs when the `if` condition is `False`:

```python
temperature = 28

if temperature > 30:
    print("Too hot")
else:
    print("Comfortable")
```

### elif

Checks multiple conditions in sequence. Only the first `True` block runs — the rest are skipped:

```python
score = 85

if score >= 90:
    print("A")
elif score >= 70:
    print("B")
elif score >= 50:
    print("C")
else:
    print("Fail")

# Output: B
```

### Nested conditionals

You can place `if` statements inside other `if` blocks. Keep nesting shallow — more than 2–3 levels makes code hard to read:

```python
age = 20
has_licence = True

# ❌ Unnecessarily nested
if age >= 18:
    if has_licence:
        print("Can drive")

# ✅ Flattened with 'and'
if age >= 18 and has_licence:
    print("Can drive")
```

### Ternary operator

A compact `if-else` on a single line for simple assignments:

```python
age = 20
status = "Adult" if age >= 18 else "Minor"

# In a print
print("Hot" if temperature > 30 else "Comfortable")

# In a list comprehension
numbers = [1, 2, 3, 4, 5]
result = [n if n % 2 == 0 else 0 for n in numbers]
# [0, 2, 0, 4, 0]
```

**When to use it:**
- ✅ Simple two-option assignments.
- ✅ When it genuinely improves readability.
- ❌ Avoid nesting ternary operators — they become unreadable fast.

---

## for loops

The `for` loop iterates over the elements of an iterable, processing each one in turn.

```python
for variable in iterable:
    # runs once per element
```

### Iterables and iterators

An **iterable** is any object that can return its elements one by one — strings, lists, tuples, dicts, sets and ranges are all iterables.

An **iterator** is the internal mechanism that tracks position during iteration. `for` loops create and use iterators automatically. You can interact with them manually:

```python
colours = ["red", "green", "blue"]
iterator = iter(colours)

next(iterator)  # "red"
next(iterator)  # "green"
next(iterator)  # "blue"
next(iterator)  # StopIteration — no more elements
```

You rarely need to do this manually, but knowing it exists helps you understand how `for` works under the hood.

### range()

`range()` generates sequences of numbers efficiently without creating a list in memory:

```python
range(stop)              # 0 to stop-1
range(start, stop)       # start to stop-1
range(start, stop, step) # start to stop-1, jumping by step
```

```python
list(range(5))          # [0, 1, 2, 3, 4]
list(range(2, 10))      # [2, 3, 4, 5, 6, 7, 8, 9]
list(range(0, 20, 2))   # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
list(range(10, 0, -1))  # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

for i in range(5):
    print(i)  # 0, 1, 2, 3, 4
```

### Iterating over common types

```python
# List
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# String — each character
for char in "Python":
    print(char)

# Dictionary
person = {"name": "Javi", "age": 29, "city": "Madrid"}

for key in person:           # keys (default)
    print(key)

for value in person.values():
    print(value)

for key, value in person.items():
    print(f"{key}: {value}")
```

### enumerate()

Gives you both the index and the value on each iteration:

```python
fruits = ["apple", "banana", "cherry"]

for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
# 0: apple
# 1: banana
# 2: cherry

# Start counting from 1
for index, fruit in enumerate(fruits, start=1):
    print(f"{index}. {fruit}")
# 1. apple
# 2. banana
# 3. cherry
```

### zip()

Combines multiple iterables element by element, like a zipper:

```python
names = ["Ana", "Juan", "María"]
ages = [25, 30, 22]

for name, age in zip(names, ages):
    print(f"{name} is {age} years old")
# Ana is 25 years old
# Juan is 30 years old
# María is 22 years old
```

```python
# Build a dictionary from two lists
keys = ["name", "age", "city"]
values = ["Javi", 29, "Madrid"]
person = dict(zip(keys, values))
# {'name': 'Javi', 'age': 29, 'city': 'Madrid'}
```

```python
# Three iterables at once
for name, age, city in zip(names, ages, cities):
    print(f"{name}, {age}, {city}")
```

**zip() stops at the shortest iterable:**

```python
names = ["Ana", "Juan", "María"]
ages = [25, 30]  # shorter

list(zip(names, ages))  # [('Ana', 25), ('Juan', 30)]
# María is dropped
```

**Unzipping with `*`:**

```python
pairs = [("Ana", 25), ("Juan", 30), ("María", 22)]
names, ages = zip(*pairs)

print(names)  # ('Ana', 'Juan', 'María')
print(ages)   # (25, 30, 22)
```

**Transposing a matrix:**

```python
matrix = [[1, 2, 3], [4, 5, 6]]
transposed = list(zip(*matrix))
# [(1, 4), (2, 5), (3, 6)]
```

### The underscore `_`

By convention, `_` means "I need this variable syntactically but I don't care about its value":

```python
# Repeat N times without using the counter
for _ in range(5):
    print("hello")

# Only care about the index
for i, _ in enumerate(names):
    print(f"Position {i}")
```

### Nested loops

```python
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} × {j} = {i * j}")
    print()

# Matrix traversal
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for row in matrix:
    for element in row:
        print(element, end=" ")
    print()
```

---

## while loops

The `while` loop repeats as long as a condition is `True`. Use it when you do not know in advance how many iterations you need.

```python
while condition:
    # runs as long as condition is True
```

> Always make sure the condition will eventually become `False`, or you will have an infinite loop.

```python
# Countdown
counter = 5
while counter > 0:
    print(counter)
    counter -= 1
# 5, 4, 3, 2, 1

# Accumulate until a limit
total = 0
n = 1
while total < 50:
    total += n
    n += 1
```

### Input validation

`while` is ideal for repeating until the user provides valid input:

```python
correct_password = "python123"
attempts = 3

while attempts > 0:
    password = input("Enter password: ")
    if password == correct_password:
        print("Access granted")
        break
    attempts -= 1
    print(f"Wrong password. {attempts} attempts remaining")

if attempts == 0:
    print("Account locked")
```

### Infinite loops

`while True` runs forever until explicitly stopped with `break`. Useful for menus and servers:

```python
while True:
    print("\n1. View data")
    print("2. Add data")
    print("3. Exit")

    option = input("Choose an option: ")

    if option == "1":
        print("Showing data...")
    elif option == "2":
        print("Adding data...")
    elif option == "3":
        print("Goodbye")
        break
    else:
        print("Invalid option")
```

### for vs while

```python
# Use for when you know the number of iterations
for i in range(10):
    print(i)

# Use while when the condition is dynamic
response = ""
while response.lower() != "quit":
    response = input("Type 'quit' to exit: ")
```

---

## Loop control

### break

Stops the loop immediately and continues with the code after it:

```python
numbers = [1, 5, 3, 8, 2]
target = 8

for number in numbers:
    if number == target:
        print(f"Found: {target}")
        break
```

### continue

Skips the rest of the current iteration and jumps to the next one:

```python
# Print only odd numbers
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)
# 1, 3, 5, 7, 9

# Skip negative values
values = [1, -2, 3, -4, 5]
for value in values:
    if value < 0:
        continue
    print(f"Processing: {value}")
```

### pass

Does absolutely nothing — a syntactic placeholder for code you have not written yet:

```python
for i in range(5):
    if i == 3:
        pass  # TODO: handle this case
    else:
        print(i)

def process_data():
    pass  # implement later

class MyClass:
    pass
```

### else in loops

A unique Python feature: the `else` block of a loop runs **only if the loop completed without hitting a `break`**. This is perfect for search patterns:

```python
# Check if a number is prime
number = 17

for i in range(2, number):
    if number % i == 0:
        print(f"{number} is not prime (divisible by {i})")
        break
else:
    print(f"{number} is prime")
# 17 is prime
```

```python
# User authentication
users = ["admin", "user1", "user2"]
username = "hacker"

for user in users:
    if user == username:
        print("User found")
        break
else:
    print("User not found")
# User not found
```

---

## Comprehensions

Comprehensions are a concise, Pythonic way to build collections from iterables. They are not just syntactic sugar — they are also faster than equivalent `for` loops because they are optimised at the interpreter level.

### List comprehensions

```python
# Traditional loop
squares = []
for i in range(10):
    squares.append(i ** 2)

# List comprehension
squares = [i ** 2 for i in range(10)]
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# With a filter condition
evens = [i for i in range(20) if i % 2 == 0]
# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# Transform strings
words = ["python", "javascript", "go"]
upper = [word.upper() for word in words]
# ['PYTHON', 'JAVASCRIPT', 'GO']

# With ternary operator
numbers = [1, 2, 3, 4, 5]
result = [n if n % 2 == 0 else 0 for n in numbers]
# [0, 2, 0, 4, 0]

# Nested — flatten a matrix
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [element for row in matrix for element in row]
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

### Dict comprehensions

```python
squares = {x: x**2 for x in range(6)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# With filter
even_squares = {x: x**2 for x in range(10) if x % 2 == 0}

# Invert key-value pairs
original = {"a": 1, "b": 2, "c": 3}
inverted = {v: k for k, v in original.items()}
# {1: 'a', 2: 'b', 3: 'c'}

# Normalise keys to lowercase
raw = {"Name": "Javi", "AGE": 29, "City": "Madrid"}
clean = {k.lower(): v for k, v in raw.items()}
# {'name': 'Javi', 'age': 29, 'city': 'Madrid'}
```

### Set comprehensions

```python
# Unique squares
unique_squares = {x**2 for x in range(-5, 6)}
# {0, 1, 4, 9, 16, 25} — no duplicates from negatives

# Unique first letters
words = ["apple", "avocado", "banana", "blueberry", "cherry"]
first_letters = {word[0] for word in words}
# {'a', 'b', 'c'}
```

### Generator expressions

A generator expression looks like a list comprehension but uses parentheses instead of brackets. The key difference: it does not build the whole collection in memory — it generates values one at a time on demand.

```python
# List comprehension — builds the entire list in memory
squares_list = [x**2 for x in range(1_000_000)]

# Generator expression — generates values one at a time
squares_gen = (x**2 for x in range(1_000_000))
```

Generators are essential in AI engineering when processing large datasets:

```python
# Sum without loading everything into memory
total = sum(x**2 for x in range(1_000_000))

# Process a large file line by line
with open("large_file.txt") as f:
    long_lines = (line for line in f if len(line) > 100)
    for line in long_lines:
        process(line)
```

**List vs generator — when to use each:**

| | List comprehension | Generator expression |
|---|---|---|
| Syntax | `[x for x in ...]` | `(x for x in ...)` |
| Memory | Builds all at once | One value at a time |
| Reusable | ✅ iterate multiple times | ❌ exhausted after one pass |
| Use when | You need the full list | You only need to iterate once |

---

## Summary

**Conditionals:**
- `if` / `elif` / `else` — only the first `True` block runs.
- Ternary: `value_if_true if condition else value_if_false`.
- Avoid deep nesting — flatten with `and` / `or` when possible.

**for loops:**
- Iterate over any iterable: lists, strings, dicts, ranges, etc.
- `range()` generates numbers efficiently without building a list.
- `enumerate()` gives index and value simultaneously.
- `zip()` combines multiple iterables in parallel.
- `_` signals an unused variable.

**while loops:**
- Repeat while a condition is `True`.
- Use for dynamic conditions and input validation.
- `while True` with `break` is the standard pattern for menus and servers.

**Loop control:**
- `break` — exit the loop immediately.
- `continue` — skip to the next iteration.
- `pass` — syntactic placeholder, does nothing.
- `else` on a loop — runs only if no `break` occurred. Great for search patterns.

**Comprehensions:**
- List: `[expr for item in iterable if condition]`
- Dict: `{key: value for item in iterable}`
- Set: `{expr for item in iterable}`
- Generator: `(expr for item in iterable)` — lazy, memory-efficient.

In the next lesson we will cover errors and exceptions — how Python signals problems and how to handle them gracefully.