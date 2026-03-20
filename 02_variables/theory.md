# 02 — Variables and Data Types

Programs need to store and manipulate information. Variables are how Python does that — named containers that hold values you can use and change throughout your code. This lesson covers variables, the main data types and how Python handles them.

---

## What is a variable?

A variable is a named space in memory that stores a value. Think of it as a labelled box where you keep information for later use.

```python
message = "Hello, world!"
print(message)  # Hello, world!
```

To create a variable, assign a descriptive name and a value using `=`. The name should be clear but not excessively long — `user_age` is better than `ua` or `the_age_of_the_registered_user`.

### Variables can change

```python
message = "Hello, world!"
print(message)  # Hello, world!

message = "Goodbye, world!"
print(message)  # Goodbye, world!
```

### Assigning variables to each other

```python
message = "Hello, world!"
message2 = message
print(message2)  # Hello, world!
```

---

## Naming rules and conventions

### Mandatory rules

- Can contain letters (A-Z, a-z), digits (0-9) and underscores (`_`).
- Cannot start with a digit — `2var` is invalid, `var2` is valid.
- Case-sensitive — `var`, `Var` and `VAR` are three different variables.
- Cannot use reserved keywords — `if`, `for`, `while`, `class`, etc.

```python
# ✅ Valid
name = "Javi"
user_age = 29
_private = 10
user2 = "Ana"

# ❌ Invalid
2name = "Error"       # Starts with a digit
my-variable = 10      # Contains a hyphen
user name = "x"       # Contains a space
class = "data"        # Reserved keyword
```

### Conventions (PEP 8)

- Variables and functions → `snake_case`: `full_name`, `user_age`
- Classes → `PascalCase`: `UserProfile`, `DataLoader`
- Constants → `UPPER_CASE`: `PI = 3.14159`, `MAX_RETRIES = 3`
- Use descriptive names — `attempt_count` over `ac`
- Avoid single-letter names except in short loops

---

## Dynamic typing

Python determines the type of a variable automatically based on the value you assign. You do not need to declare types explicitly — this is called **dynamic typing**.

```python
x = 42          # int
x = 3.14        # now float
x = "hello"     # now str
```

You can check the type of any variable with `type()`:

```python
print(type(42))        # <class 'int'>
print(type(3.14))      # <class 'float'>
print(type("hello"))   # <class 'str'>
print(type(True))      # <class 'bool'>
print(type(None))      # <class 'NoneType'>
```

---

## Strings

A string is a sequence of characters — any text enclosed in quotes.

```python
message = "This is a string"
message2 = 'This is also a string'
```

### Single vs double quotes

Both work identically. The flexibility lets you include one type of quote inside the other:

```python
phrase1 = "It's a great day"
phrase2 = 'She said "hello"'
```

### Escape sequences

When you need to use the same type of quote inside the string, use the escape character `\`:

```python
message = "She said: \"hello\""
message2 = 'It\'s a great day'
```

Other useful escape sequences:

| Sequence | Meaning |
|---|---|
| `\n` | New line |
| `\t` | Tab |
| `\\` | Literal backslash |
| `\"` | Literal double quote |
| `\'` | Literal single quote |

### Multi-line strings

Use triple quotes for strings that span multiple lines:

```python
message = """First line
Second line
Third line"""

print(message)
# First line
# Second line
# Third line
```

Triple quotes are also used for **docstrings** — documentation inside functions and classes:

```python
def greet(name):
    """
    Greets a person by name.

    Args:
        name: The name of the person to greet.
    """
    print(f"Hello, {name}!")
```

---

## String indexing and slicing

Strings are ordered sequences. Each character has a position called an **index**, starting at 0.

```python
word = "Python"

# Positive indices (left to right)
word[0]   # 'P'
word[1]   # 'y'
word[5]   # 'n'

# Negative indices (right to left)
word[-1]  # 'n' (last character)
word[-2]  # 'o' (second to last)
```

```
String:     P    y    t    h    o    n
Positive:   0    1    2    3    4    5
Negative:  -6   -5   -4   -3   -2   -1
```

### Slicing

Slicing extracts a portion of a string using `[start:end]`. The end index is **not** included.

```python
word = "Python"

word[0:3]   # 'Pyt' (indices 0, 1, 2)
word[2:5]   # 'tho' (indices 2, 3, 4)
word[:3]    # 'Pyt' (from start to index 2)
word[3:]    # 'hon' (from index 3 to end)
word[:]     # 'Python' (full copy)
word[-3:]   # 'hon' (last 3 characters)
```

### Stride

The full slice syntax is `[start:end:step]`. The step controls how many positions to jump:

```python
word = "Python"

word[::2]   # 'Pto' (every 2 characters)
word[::-1]  # 'nohtyP' (reverse the string)
```

### Strings are immutable

You cannot modify individual characters of a string. To "change" a string, create a new one:

```python
word = "Python"
word[0] = "J"  # ❌ TypeError

# ✅ Create a new string instead
new_word = "J" + word[1:]  # 'Jython'
```

---

## String operations

### Concatenation

```python
first_name = "Javi"
last_name = "García"
full_name = first_name + " " + last_name  # "Javi García"
```

### Repetition

```python
separator = "-" * 20   # "--------------------"
echo = "hello " * 3   # "hello hello hello "
```

### Length

```python
word = "Python"
print(len(word))  # 6
```

---

## Numbers

Python has three numeric types: `int`, `float` and `complex`.

### Integers (int)

Whole numbers without a decimal part.

```python
age = 29
temperature = -5
population = 1_000_000  # Underscores improve readability
```

Python integers have no practical size limit — only your system memory.

**int vs str:**

```python
number = 10     # int — you can do math
text = "10"     # str — just text

number + 5      # 15 ✅
text + 5        # ❌ TypeError
```

**Casting to int:**

```python
int("42")    # 42
int(3.9)     # 3 (truncates, does not round)
int("hello") # ❌ ValueError
```

### Floats (float)

Numbers with a decimal part.

```python
price = 19.99
pi = 3.14159
speed_of_light = 3e8  # Scientific notation: 3 × 10^8
```

**Casting to float:**

```python
float("3.14")  # 3.14
float(5)       # 5.0
```

**Precision warning:**

Floats have binary representation limits. This is a well-known property of floating-point arithmetic:

```python
0.1 + 0.2  # 0.30000000000000004

# For comparisons, use math.isclose()
import math
math.isclose(0.1 + 0.2, 0.3)  # True
```

**Formatting floats:**

```python
number = 123.456789

print(f"{number:.2f}")       # 123.46
print(f"{number:.4f}")       # 123.4568
print(f"{1_234_567.89:,.2f}") # 1,234,567.89
print(f"{0.1567:.2%}")       # 15.67%
```

### Complex numbers (complex)

Numbers with a real and an imaginary part, written with `j`. Useful in scientific computing and signal processing — less common in day-to-day AI engineering.

```python
z = 3 + 4j
z.real   # 3.0
z.imag   # 4.0
abs(z)   # 5.0 (magnitude)
```

---

## Booleans

Booleans represent truth values. There are only two: `True` and `False`.

```python
is_active = True
is_empty = False
```

`True` and `False` are reserved keywords and must be capitalised.

### Comparison operators return booleans

```python
age = 29

age > 18   # True
age < 18   # False
age == 29  # True
age != 30  # True
```

### Logical operators

```python
has_licence = True
has_car = False

has_licence and has_car   # False
has_licence or has_car    # True
not has_car               # True
```

### Truthiness and falsiness

In Python, any value can be evaluated in a boolean context. This is called **truthiness**.

**Falsy values** — evaluate to `False`:
- `False`, `None`
- `0`, `0.0`, `0j`
- Empty sequences: `""`, `[]`, `()`, `{}`

**Everything else is truthy:**

```python
bool(0)       # False
bool(1)       # True
bool("")      # False
bool("hello") # True
bool([])      # False
bool([1, 2])  # True
```

This is useful in conditionals:

```python
name = ""
if not name:
    print("Name is empty")
```

---

## None

`None` represents the **absence of a value**. It is the only value of type `NoneType`.

```python
result = None
user = None
```

### When to use None

```python
# Uninitialised variable
name = None

# A function with no explicit return gives back None
def greet():
    print("Hello")

result = greet()  # None

# Default parameter value
def process(data=None):
    if data is None:
        data = []
```

### None is not the same as other empty values

```python
None == False  # False
None == 0      # False
None == ""     # False
None == []     # False
```

### Always use `is` to compare with None

```python
result = None

# ✅ Correct
if result is None:
    print("No result")

if result is not None:
    print("Got a result")

# ⚠️ Works but not recommended
if result == None:
    print("No result")
```

`None` is falsy:

```python
value = None
if not value:
    print("Value is None or empty")  # Prints
```

---

## Summary

- A variable is a named container for a value. Use `snake_case` for names.
- Python uses dynamic typing — no need to declare types explicitly.
- Use `type()` to check the type of any variable.
- Strings are immutable sequences of characters. Access characters with indices, extract portions with slicing.
- Use `int` for whole numbers, `float` for decimals. Be aware of float precision limits.
- Booleans are `True` or `False`. Any value has a truthiness — know which values are falsy.
- `None` represents the absence of a value. Always compare with `is`, not `==`.

In the next lesson we will cover operators — how Python lets you compute and compare values.