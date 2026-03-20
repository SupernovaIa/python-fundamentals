# 04 — Data Structures

Programs need to organise information, not just store individual values. Python has four built-in data structures that cover almost every situation: lists, tuples, dictionaries and sets. Choosing the right one makes your code faster, cleaner and easier to maintain.

---

## Lists

Lists are the most versatile data structure in Python — ordered, mutable and capable of holding any mix of types.

### Key characteristics

- **Ordered** — maintain insertion order.
- **Mutable** — you can add, modify and remove elements after creation.
- **Allow duplicates** — the same value can appear multiple times.
- **Heterogeneous** — can mix any data types.
- **Indexed** — access elements by position.

### Creating lists

```python
# Empty list
empty = []
empty2 = list()

# List with elements
numbers = [1, 2, 3, 4, 5]
names = ["Ana", "Juan", "María"]

# Mixed types
mixed = [1, "hello", 3.14, True, None]

# Duplicates are allowed
duplicates = [1, 2, 2, 3, 3, 3]
```

### Converting to list

```python
list("Python")    # ['P', 'y', 't', 'h', 'o', 'n']
list((1, 2, 3))   # [1, 2, 3]
list(range(5))    # [0, 1, 2, 3, 4]
```

### Accessing elements

Indexing and slicing work exactly as with strings (covered in lesson `02_variables`):

```python
items = ["Data", "Marketing", "UX", "Web", "MBA"]

items[0]    # "Data"
items[-1]   # "MBA"
items[1:4]  # ["Marketing", "UX", "Web"]
items[::-1] # ["MBA", "Web", "UX", "Marketing", "Data"]
```

### Modifying lists

```python
fruits = ["apple", "banana", "cherry"]

# Change a single element
fruits[1] = "orange"
# ["apple", "orange", "cherry"]

# Replace a slice
fruits[0:2] = ["kiwi", "mango"]
# ["kiwi", "mango", "cherry"]
```

### Adding elements

```python
fruits = ["apple", "banana"]

fruits.append("cherry")         # add to the end
fruits.insert(1, "orange")      # insert at index 1
fruits.extend(["grape", "pear"]) # add multiple elements
```

### Removing elements

```python
items = ["Data", "Marketing", "UX", "Web", "MBA"]

del items[1]          # remove by index
items.remove("UX")    # remove by value (first occurrence)
last = items.pop()    # remove and return last element
first = items.pop(0)  # remove and return element at index 0
items.clear()         # remove all elements
```

### Useful functions and methods

```python
numbers = [3, 1, 4, 1, 5, 9, 2, 6]

len(numbers)        # 8
min(numbers)        # 1
max(numbers)        # 9
sum(numbers)        # 31
numbers.count(1)    # 2 — number of occurrences
numbers.index(5)    # 4 — index of first occurrence
4 in numbers        # True
10 in numbers       # False
```

### Sorting

```python
numbers = [3, 1, 4, 1, 5, 9]

# sort() — modifies the list in place
numbers.sort()               # [1, 1, 3, 4, 5, 9]
numbers.sort(reverse=True)   # [9, 5, 4, 3, 1, 1]

# sorted() — returns a new sorted list, original unchanged
original = [3, 1, 4, 1, 5, 9]
ordered = sorted(original)   # [1, 1, 3, 4, 5, 9]
print(original)              # [3, 1, 4, 1, 5, 9]
```

### Copying lists

A simple assignment does not copy a list — it creates another reference to the same object:

```python
original = [1, 2, 3]

# ❌ This does NOT copy — both variables point to the same list
reference = original
reference[0] = 999
print(original)  # [999, 2, 3]

# ✅ These all create independent copies
copy1 = original[:]
copy2 = list(original)
copy3 = original.copy()

# For nested lists, use deepcopy
import copy
nested = [[1, 2], [3, 4]]
deep = copy.deepcopy(nested)
```

### Nested lists

Lists can contain other lists, which is useful for matrices and tables:

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix[0]       # [1, 2, 3]
matrix[1][2]    # 6
matrix[-1][-1]  # 9
```

### List comprehensions

A concise way to create lists from transformations or filters (covered in depth in lesson `06_control_flow`):

```python
squares = [i ** 2 for i in range(10)]
evens = [i for i in range(20) if i % 2 == 0]
```

---

## Tuples

Tuples are the immutable siblings of lists. Once created, they cannot be changed. This restriction is actually their strength.

### Key characteristics

- **Ordered** — maintain insertion order.
- **Immutable** — cannot be modified after creation.
- **Allow duplicates** — same value can appear multiple times.
- **Indexed** — access by position, slicing works the same as lists.
- **Slightly faster** — less memory and overhead than lists.

### When to use tuples

- Data that should not change: coordinates, dates, config values.
- Dictionary keys (lists cannot be used as keys).
- Returning multiple values from a function safely.
- Protecting data from accidental modification.

### Creating tuples

```python
empty = ()
empty2 = tuple()

coordinates = (10.5, 20.3)
colours = ("red", "green", "blue")
mixed = (1, "hello", 3.14)

# ⚠️ Single-element tuple needs a trailing comma
not_a_tuple = (5)    # int
is_a_tuple = (5,)    # tuple
```

### Immutability

```python
coordinates = (10, 20)

coordinates[0] = 15       # ❌ TypeError
coordinates.append(30)    # ❌ AttributeError
del coordinates[0]        # ❌ TypeError
```

Note: if a tuple contains a mutable object like a list, that object can still be modified:

```python
t = (1, 2, [3, 4])
t[2].append(5)   # ✅ modifies the list inside
print(t)         # (1, 2, [3, 4, 5])
t[2] = [99]      # ❌ TypeError — cannot reassign the tuple element
```

### Tuple unpacking

One of the most useful features of tuples:

```python
coordinates = (10, 20)
x, y = coordinates

# Swap without a temporary variable
a, b = 5, 10
a, b = b, a  # a=10, b=5

# Extended unpacking
numbers = (1, 2, 3, 4, 5)
first, *middle, last = numbers
print(first)   # 1
print(middle)  # [2, 3, 4]
print(last)    # 5

# Unpacking function return values
def get_user():
    return "Javi", 29, "Madrid"

name, age, city = get_user()
```

### Operations

```python
t1 = (1, 2, 3)
t2 = (4, 5, 6)

t1 + t2        # (1, 2, 3, 4, 5, 6) — concatenation (new tuple)
(0,) * 5       # (0, 0, 0, 0, 0) — repetition
len(t1)        # 3
min(t1)        # 1
max(t1)        # 3
sum(t1)        # 6
t1.count(2)    # 1
t1.index(3)    # 2
2 in t1        # True
```

---

## Dictionaries

Dictionaries associate keys with values. Think of them as a contact book — you look up a name (key) to get a phone number (value). Lookups are instantaneous regardless of size.

### Key characteristics

- **Ordered** — maintain insertion order (Python 3.7+).
- **Mutable** — add, modify and remove key-value pairs freely.
- **Unique keys** — duplicate keys overwrite the previous value.
- **Immutable keys** — keys must be immutable types: `str`, `int`, `float`, `tuple`.
- **Any value type** — values can be lists, dicts, objects, anything.
- **O(1) lookup** — finding a value by key is instant.

### Creating dictionaries

```python
empty = {}
empty2 = dict()

person = {
    "name": "Javi",
    "age": 29,
    "city": "Madrid"
}

# Using dict()
person2 = dict(name="Ana", age=25, city="Barcelona")

# ❌ Lists cannot be keys (they are mutable)
# invalid = {[1, 2]: "value"}  # TypeError
```

### Accessing values

```python
person = {"name": "Javi", "age": 29, "city": "Madrid"}

person["name"]   # "Javi"
person["age"]    # 29

# ❌ KeyError if key does not exist
# person["surname"]

# ✅ get() returns None if key does not exist
person.get("surname")             # None
person.get("surname", "Unknown")  # "Unknown"
```

### Adding and updating elements

```python
person = {"name": "Javi", "age": 29}

# Add new key-value pair
person["city"] = "Madrid"

# Update existing value
person["age"] = 30

# Update multiple values at once
person.update({"city": "Barcelona", "role": "AI Engineer"})
```

### Removing elements

```python
person = {"name": "Javi", "age": 29, "city": "Madrid", "role": "AI Engineer"}

del person["role"]                        # remove by key
age = person.pop("age")                   # remove and return value
phone = person.pop("phone", "N/A")        # remove with default if missing
last = person.popitem()                   # remove and return last inserted pair
person.clear()                            # remove all elements
```

### Checking for keys

```python
person = {"name": "Javi", "age": 29}

"name" in person      # True
"surname" in person   # False
"surname" not in person  # True

# ⚠️ 'in' checks keys, not values
"Javi" in person      # False
```

### Iterating over dictionaries

```python
person = {"name": "Javi", "age": 29, "city": "Madrid"}

for key in person:
    print(key)

for key in person.keys():
    print(key)

for value in person.values():
    print(value)

for key, value in person.items():
    print(f"{key}: {value}")
```

### Useful methods

```python
person = {"name": "Javi", "age": 29, "city": "Madrid"}

list(person.keys())    # ['name', 'age', 'city']
list(person.values())  # ['Javi', 29, 'Madrid']
list(person.items())   # [('name', 'Javi'), ('age', 29), ('city', 'Madrid')]
len(person)            # 3
```

### Nested dictionaries

```python
company = {
    "name": "Acme",
    "employees": {
        "javi": {"age": 29, "role": "AI Engineer"},
        "ana": {"age": 27, "role": "Data Scientist"}
    },
    "offices": ["Madrid", "Barcelona"]
}

company["employees"]["javi"]["role"]  # "AI Engineer"
company["offices"][0]                 # "Madrid"
```

### Dictionary comprehensions

```python
squares = {x: x**2 for x in range(6)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

even_squares = {x: x**2 for x in range(10) if x % 2 == 0}

original = {"a": 1, "b": 2, "c": 3}
inverted = {v: k for k, v in original.items()}
# {1: "a", 2: "b", 3: "c"}
```

---

## Sets

Sets are unordered collections of unique elements. They automatically discard duplicates and support mathematical set operations.

### Key characteristics

- **Unordered** — no guaranteed order, cannot access by index.
- **Unique elements** — duplicates are silently ignored.
- **Mutable** — add and remove elements freely.
- **Immutable elements** — can only contain hashable types: `int`, `str`, `tuple`.
- **O(1) membership check** — checking if an element exists is instant.

### Creating sets

```python
# ⚠️ {} creates a dict, not a set — use set() for empty sets
empty = set()

colours = {"red", "blue", "green"}

# From a list — duplicates removed automatically
numbers = set([1, 2, 2, 3, 3, 3, 4])
print(numbers)  # {1, 2, 3, 4}

# From a string — unique characters
letters = set("python")
# {'p', 'y', 't', 'h', 'o', 'n'} — order is arbitrary
```

### Adding and removing elements

```python
colours = {"red", "blue"}

colours.add("green")       # add one element
colours.add("red")         # duplicate — no effect
colours.update(["yellow", "black"])  # add multiple elements

colours.remove("blue")     # ❌ KeyError if not found
colours.discard("purple")  # ✅ no error if not found
element = colours.pop()    # remove and return an arbitrary element
colours.clear()            # remove all elements
```

### Set operations

This is where sets shine — mathematical operations on collections:

```python
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}

# Union — elements in a OR b
a | b              # {1, 2, 3, 4, 5, 6, 7, 8}
a.union(b)

# Intersection — elements in a AND b
a & b              # {4, 5}
a.intersection(b)

# Difference — elements in a but NOT in b
a - b              # {1, 2, 3}
a.difference(b)

# Symmetric difference — in a OR b, but NOT both
a ^ b              # {1, 2, 3, 6, 7, 8}
a.symmetric_difference(b)
```

### Set relationships

```python
a = {1, 2, 3}
b = {1, 2, 3, 4, 5}
c = {6, 7, 8}

a.issubset(b)    # True  — all elements of a are in b
b.issuperset(a)  # True  — b contains all elements of a
a.isdisjoint(c)  # True  — no elements in common
a.isdisjoint(b)  # False — they share 1, 2, 3
```

### Frozensets

An immutable version of a set. Can be used as a dictionary key or stored inside another set:

```python
frozen = frozenset([1, 2, 3])
# frozen.add(4)  # ❌ AttributeError

d = {frozen: "value"}  # ✅ valid as a dict key
```

---

## Choosing the right structure

| | List | Tuple | Dictionary | Set |
|---|---|---|---|---|
| Ordered | ✅ | ✅ | ✅ (3.7+) | ❌ |
| Mutable | ✅ | ❌ | ✅ | ✅ |
| Duplicates | ✅ | ✅ | ❌ (keys) | ❌ |
| Indexed | ✅ | ✅ | By key | ❌ |
| Syntax | `[1, 2]` | `(1, 2)` | `{"k": "v"}` | `{1, 2}` |

**Use a list** when you need an ordered, modifiable collection — your default choice.  
**Use a tuple** when data should not change, or when you need an immutable sequence.  
**Use a dictionary** when you need to associate keys with values and look them up fast.  
**Use a set** when uniqueness matters or you need set operations.

---

## Summary

- Lists are ordered and mutable — the most flexible structure. Use `append`, `extend`, `remove`, `pop` and `sort` to manipulate them.
- Tuples are ordered and immutable. Use them for data that should not change. Unpacking is one of their most useful features.
- Dictionaries map keys to values with O(1) lookup. Use `get()` instead of direct access when a key might not exist.
- Sets store unique elements and support fast membership checks and mathematical set operations.
- Copying lists requires explicit methods (`[:]`, `list()`, `.copy()`) — assignment only creates a reference.

In the next lesson we will cover Python's built-in methods — the functions that come built into every data type.