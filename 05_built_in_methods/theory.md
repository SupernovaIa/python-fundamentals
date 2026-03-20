# 05 — Built-in Methods

Python's built-in types come with a rich set of methods that cover the most common operations you'll need. This lesson focuses on the methods not yet covered in previous lessons, with particular depth on string methods — the largest and most varied group.

> **Key distinction**: methods on immutable types (strings, tuples) always return a new object. Methods on mutable types (lists, dicts, sets) often modify the object in place and return `None`.

---

## String methods

Strings are immutable — every method returns a new string, the original is never changed.

### Case transformation

```python
text = "hello world"

text.upper()       # "HELLO WORLD"
text.lower()       # "hello world"
text.capitalize()  # "Hello world" — first letter upper, rest lower
text.title()       # "Hello World" — first letter of each word upper
text.swapcase()    # "HELLO WORLD" → "hello world" and vice versa
```

**Practical use — case-insensitive comparison:**

```python
user_input = "PYTHON"
if user_input.lower() == "python":
    print("Correct")
```

> ⚠️ `title()` does not handle apostrophes well: `"it's fine".title()` → `"It'S Fine"`.

### Stripping whitespace and characters

```python
text = "   hello world   "

text.strip()    # "hello world"  — both sides
text.lstrip()   # "hello world   " — left only
text.rstrip()   # "   hello world" — right only

# Strip specific characters
"###hello###".strip("#")     # "hello"
"--hello--".strip("-")       # "hello"
"xyz hello xyz".strip("xyz ") # "hello"
```

**Common use case — cleaning user input:**

```python
email = "  user@example.com  "
clean = email.strip().lower()  # "user@example.com"
```

### Searching

```python
text = "Python is great, Python is popular"

# find() — returns index of first match, -1 if not found
text.find("Python")     # 0
text.find("Java")       # -1

# rfind() — same but searches from the right
text.rfind("Python")    # 17

# count() — number of non-overlapping occurrences
text.count("Python")    # 2
text.count("is")        # 2

# startswith() / endswith()
"report.pdf".startswith("report")   # True
"report.pdf".endswith(".pdf")       # True
"report.pdf".endswith((".pdf", ".doc", ".txt"))  # True — tuple of options
```

**`find()` vs `index()`:**

```python
text = "hello"
text.find("z")    # -1 — safe, no exception
text.index("z")   # ValueError — raises an exception
```

Use `find()` when the substring might not be there. Use `index()` when its absence would be a bug.

### Replacing

```python
text = "I like Python. Python is great."

text.replace("Python", "JavaScript")
# "I like JavaScript. JavaScript is great."

# Limit the number of replacements
text.replace("Python", "Go", 1)
# "I like Go. Python is great."
```

### Splitting and joining

```python
# split() — string to list
"Python is great".split()        # ['Python', 'is', 'great']
"2026-01-15".split("-")          # ['2026', '01', '15']
"a,b,c,d".split(",", 2)         # ['a', 'b', 'c,d'] — max 2 splits
"line1\nline2\nline3".split("\n") # ['line1', 'line2', 'line3']

# splitlines() — split by line breaks
"line1\nline2\r\nline3".splitlines()  # ['line1', 'line2', 'line3']

# rsplit() — split from the right
"a,b,c,d".rsplit(",", 1)  # ['a,b,c', 'd']
```

```python
# join() — list to string
words = ["Python", "is", "great"]
" ".join(words)    # "Python is great"
"-".join(words)    # "Python-is-great"
"".join(words)     # "Pythonisgreat"

# join is always called on the separator, not the list
parts = ["home", "user", "documents"]
"/".join(parts)    # "home/user/documents"

# Only works with lists of strings
numbers = [1, 2, 3]
",".join(str(n) for n in numbers)  # "1,2,3"
```

### Validation methods

These return `True` or `False` and are useful for input validation:

```python
"Python".isalpha()      # True  — all letters
"Python3".isalpha()     # False — contains digit
"12345".isdigit()       # True  — all digits
"123.45".isdigit()      # False — dot is not a digit
"Python3".isalnum()     # True  — letters or digits
"Python 3".isalnum()    # False — space is neither
"   ".isspace()         # True  — only whitespace
"hello".islower()       # True
"HELLO".isupper()       # True
"hello123".islower()    # True  — digits are ignored
```

**Practical use — validating user input:**

```python
username = input("Enter username: ")
if not username.isalnum():
    print("Username can only contain letters and digits")
```

### f-strings and formatting

f-strings (Python 3.6+) are the recommended way to format strings:

```python
name = "Javi"
age = 29
price = 1234.5678

# Basic
f"My name is {name} and I am {age} years old"

# Expressions inside braces
f"Double my age: {age * 2}"

# Method calls
f"Uppercase: {name.upper()}"

# Number formatting
f"{price:.2f}"          # "1234.57"    — 2 decimal places
f"{price:,.2f}"         # "1,234.57"   — thousands separator
f"{0.1567:.2%}"         # "15.67%"     — percentage
f"{age:05}"             # "00029"      — zero-padded

# Alignment
f"{name:>10}"   # "      Javi"  — right-aligned, width 10
f"{name:<10}"   # "Javi      "  — left-aligned
f"{name:^10}"   # "   Javi   "  — centred
f"{name:-^10}"  # "---Javi---"  — centred with fill character
```

**`str.format()` — older but still common in codebases:**

```python
"Hello, {}!".format("Javi")
"Hello, {name}!".format(name="Javi")
"Price: {:.2f}".format(1234.5678)
```

### Alignment and padding

```python
"Python".center(20)        # "       Python       "
"Python".center(20, "-")   # "-------Python-------"
"Python".ljust(20, ".")    # "Python.............."
"Python".rjust(20, ".")    # "..............Python"
"42".zfill(5)              # "00042"
"-42".zfill(5)             # "-0042" — respects the sign
```

### Raw strings

Prefix `r` before a string to treat backslashes as literal characters:

```python
# Without raw string — \n and \t are escape sequences
normal = "C:\new_folder\tab_data"
print(normal)   # C:
                # ew_folder	ab_data  (interpreted escapes)

# With raw string — backslashes are literal
path = r"C:\new_folder\tab_data"
print(path)     # C:\new_folder\tab_data

# Common use: Windows paths and regular expressions
import re
pattern = r"\d+\.\d+"  # matches "3.14", "2.71", etc.
```

---

## List methods

The core list methods (`append`, `extend`, `insert`, `remove`, `pop`, `clear`, `sort`, `reverse`) were covered in lesson `04_data_structures`. This section focuses on what was not yet covered.

### Sorting with a key function

`sort()` and `sorted()` accept a `key` parameter — a function applied to each element before comparing:

```python
words = ["banana", "apple", "fig", "cherry"]

# Sort by length
words.sort(key=len)
print(words)  # ['fig', 'apple', 'banana', 'cherry']

# Sort alphabetically ignoring case
words = ["Banana", "apple", "Fig", "cherry"]
words.sort(key=str.lower)
print(words)  # ['apple', 'Banana', 'cherry', 'Fig']

# Sort list of dicts by a field
users = [
    {"name": "Carlos", "age": 35},
    {"name": "Ana", "age": 28},
    {"name": "Beatriz", "age": 31}
]
users.sort(key=lambda u: u["age"])
# [{"name": "Ana", ...}, {"name": "Beatriz", ...}, {"name": "Carlos", ...}]
```

`sorted()` works the same way but returns a new list without modifying the original:

```python
original = [3, 1, 4, 1, 5]
ordered = sorted(original, reverse=True)
print(original)  # [3, 1, 4, 1, 5] — unchanged
print(ordered)   # [5, 4, 3, 1, 1]
```

### copy()

Creates a shallow copy — a new list object with the same elements:

```python
original = [1, 2, 3]
copy = original.copy()
copy[0] = 999
print(original)  # [1, 2, 3] — unchanged

# Equivalent forms
copy = original[:]
copy = list(original)
```

For nested lists, use `copy.deepcopy()` (covered in lesson `04_data_structures`).

---

## Tuple methods

Tuples have only two methods, since they are immutable:

```python
t = (1, 2, 3, 2, 2, 4)

t.count(2)    # 3 — number of occurrences
t.index(3)    # 2 — index of first occurrence
t.index(2, 2) # 3 — search starting from index 2

# index() raises ValueError if not found
try:
    t.index(10)
except ValueError:
    print("Element not found")
```

---

## Dictionary methods

The core dict methods (`get`, `update`, `pop`, `popitem`, `clear`, `keys`, `values`, `items`) were covered in lesson `04_data_structures`. This section adds the remaining ones.

### setdefault()

Returns the value for a key if it exists. If it does not, inserts the key with a default value and returns it:

```python
person = {"name": "Javi"}

person.setdefault("name", "Unknown")  # "Javi" — key exists, no change
person.setdefault("age", 29)          # 29 — key added
print(person)  # {"name": "Javi", "age": 29}
```

**Practical use — building a grouped dictionary:**

```python
words = ["apple", "banana", "avocado", "blueberry", "cherry"]
grouped = {}

for word in words:
    letter = word[0]
    grouped.setdefault(letter, []).append(word)

print(grouped)
# {'a': ['apple', 'avocado'], 'b': ['banana', 'blueberry'], 'c': ['cherry']}
```

### fromkeys()

Creates a new dictionary from an iterable of keys, with an optional default value:

```python
keys = ["name", "age", "city"]

dict.fromkeys(keys)        # {'name': None, 'age': None, 'city': None}
dict.fromkeys(keys, 0)     # {'name': 0, 'age': 0, 'city': 0}
dict.fromkeys(keys, "N/A") # {'name': 'N/A', 'age': 'N/A', 'city': 'N/A'}
```

> ⚠️ Avoid using mutable defaults like `[]` — all keys will share the same list object:
> ```python
> d = dict.fromkeys(["a", "b"], [])
> d["a"].append(1)
> print(d)  # {'a': [1], 'b': [1]} — both changed!
> ```

### copy()

Creates a shallow copy of the dictionary:

```python
original = {"a": 1, "b": 2}
copy = original.copy()
copy["a"] = 100
print(original)  # {"a": 1, "b": 2} — unchanged
```

---

## Set methods — in-place operations

The core set methods and mathematical operations were covered in lesson `04_data_structures`. Python also provides in-place versions that modify the original set:

```python
a = {1, 2, 3}
b = {3, 4, 5}

# union in-place
a |= b           # a = {1, 2, 3, 4, 5}
a.update(b)      # same

# intersection in-place
a = {1, 2, 3}
a &= b           # a = {3}
a.intersection_update(b)  # same

# difference in-place
a = {1, 2, 3}
a -= b           # a = {1, 2}
a.difference_update(b)    # same

# symmetric difference in-place
a = {1, 2, 3}
a ^= b           # a = {1, 2, 4, 5}
a.symmetric_difference_update(b)  # same
```

---

## Summary — modifies vs returns new

| Type | Modifies original | Returns new object |
|---|---|---|
| **str** | never | always |
| **list** | `append`, `extend`, `insert`, `remove`, `pop`, `sort`, `reverse`, `clear` | `copy`, `count`, `index` |
| **tuple** | never | `count`, `index` |
| **dict** | `update`, `pop`, `popitem`, `clear`, `setdefault` | `get`, `keys`, `values`, `items`, `copy`, `fromkeys` |
| **set** | `add`, `update`, `remove`, `discard`, `pop`, `clear`, `|=`, `&=`, `-=`, `^=` | `union`, `intersection`, `difference`, `copy` |

> **Rule of thumb**: if a method modifies a mutable object in place, it returns `None`. Assigning the result of `list.sort()` or `list.reverse()` to a variable is a common mistake.
>
> ```python
> numbers = [3, 1, 2]
> result = numbers.sort()  # ❌ result is None
> numbers.sort()           # ✅ numbers is now sorted
> result = sorted(numbers) # ✅ result is a new sorted list
> ```

You can always explore available methods using `dir()` and read their documentation with `help()`:

```python
dir("hello")          # lists all string methods
help(str.replace)     # shows full documentation
```

In the next lesson we will cover control flow — conditionals, loops and comprehensions.