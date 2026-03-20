# 03 — Operators

Operators are special symbols that perform operations on values and variables. Python has several categories of operators, each serving a different purpose. This lesson covers all of them.

---

## Arithmetic operators

Arithmetic operators perform mathematical operations on numeric values.

```python
a = 10
b = 3
```

| Operator | Name | Example | Result |
|---|---|---|---|
| `+` | Addition | `a + b` | `13` |
| `-` | Subtraction | `a - b` | `7` |
| `*` | Multiplication | `a * b` | `30` |
| `/` | Division | `a / b` | `3.3333...` |
| `//` | Floor division | `a // b` | `3` |
| `%` | Modulo | `a % b` | `1` |
| `**` | Exponentiation | `a ** b` | `1000` |

### Division always returns a float

```python
10 / 2    # 5.0 — not 5
type(10 / 2)  # <class 'float'>
```

### Floor division

Returns only the integer part, discarding any remainder:

```python
10 // 3   # 3
7 // 2    # 3
-10 // 3  # -4 (rounds down, not towards zero)
```

### Modulo

Returns the remainder of the division:

```python
10 % 3   # 1  (10 = 3×3 + 1)
15 % 5   # 0  (exact division)
7 % 2    # 1  (7 = 2×3 + 1)
```

Common use cases:
- Check if a number is even or odd: `n % 2 == 0`
- Get the last digit of a number: `n % 10`
- Cycle through values: `index % length`

### Exponentiation

```python
2 ** 3    # 8
5 ** 2    # 25
4 ** 0.5  # 2.0 (square root)
10 ** 0   # 1
```

### Order of operations

Python follows the standard mathematical order (PEMDAS):

1. Parentheses
2. Exponentiation
3. Multiplication and division (left to right)
4. Addition and subtraction (left to right)

```python
2 + 3 * 4      # 14 (not 20 — * before +)
(2 + 3) * 4    # 20
2 ** 3 ** 2    # 512 (exponentiation is right to left)
(2 ** 3) ** 2  # 64
```

---

## String operators

Strings support two operators: concatenation and repetition.

### Concatenation with `+`

```python
greeting = "Hello" + " " + "World"  # "Hello World"
full_name = "Ada" + " " + "Lovelace"  # "Ada Lovelace"
```

You can only concatenate strings with strings:

```python
# ❌ TypeError
text = "I am " + 29 + " years old"

# ✅ Cast to string first
text = "I am " + str(29) + " years old"

# ✅ Better — use f-strings
age = 29
text = f"I am {age} years old"
```

### Repetition with `*`

```python
separator = "-" * 20   # "--------------------"
echo = "hello " * 3   # "hello hello hello "
```

---

## Assignment operators

The basic assignment operator `=` assigns a value to a variable.

```python
x = 10
name = "Javi"
is_valid = True
```

### Augmented assignment

Python lets you combine arithmetic operators with assignment to update a variable in place:

```python
x = 10
x += 5   # x = x + 5  → 15
x -= 3   # x = x - 3  → 12
x *= 2   # x = x * 2  → 24
x /= 4   # x = x / 4  → 6.0
x //= 2  # x = x // 2 → 3.0
x %= 2   # x = x % 2  → 1.0
x **= 3  # x = x ** 3 → 1.0
```

Also works with strings:

```python
message = "Hello"
message += " World"  # "Hello World"

pattern = "*"
pattern *= 5  # "*****"
```

### Multiple assignment

```python
# Assign the same value to multiple variables
x = y = z = 0

# Unpack multiple values at once
x, y, z = 1, 2, 3
name, age = "Javi", 29

# Swap values without a temporary variable
a, b = 10, 20
a, b = b, a  # a=20, b=10
```

---

## Comparison operators

Comparison operators evaluate the relationship between two values and always return a boolean (`True` or `False`).

```python
a = 10
b = 5

a > b    # True
a < b    # False
a >= 10  # True
b <= 4   # False
a == 10  # True
a != b   # True
```

### Chained comparisons

Python allows natural chaining of comparisons:

```python
age = 25

# Instead of:
if age >= 18 and age <= 65:
    print("Working age")

# You can write:
if 18 <= age <= 65:
    print("Working age")

x = 5
1 < x < 10   # True
1 < x < 3    # False
```

### String comparison

Strings are compared **lexicographically** using Unicode values:

```python
"a" < "b"          # True
"apple" < "banana" # True (a < b)
"app" < "apple"    # True (shorter string is lesser)
"A" < "a"          # True (uppercase comes before lowercase in Unicode)
```

Useful functions for understanding character ordering:

```python
ord("A")   # 65  — Unicode value of 'A'
ord("a")   # 97  — Unicode value of 'a'
chr(65)    # 'A' — character from Unicode value
chr(97)    # 'a'
```

### Comparing different types

```python
5 == 5.0    # True  (int and float with same value)
"5" == 5    # False (str vs int)
True == 1   # True  (bool is treated as int)
False == 0  # True
```

---

## Identity operators

Identity operators check whether two variables point to the **same object in memory**, not just whether they have the same value.

### `is` and `is not`

```python
a = [1, 2, 3]
b = [1, 2, 3]
c = a

a == b   # True  — same content
a is b   # False — different objects in memory
a is c   # True  — c points to the same object as a
```

You can inspect memory addresses with `id()`:

```python
print(id(a))  # e.g. 140234567891234
print(id(b))  # different address
print(id(c))  # same address as a
```

### The most important use case: comparing with None

`None` is a singleton — there is only one `None` object in memory. Always use `is` to compare with it:

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

---

## Membership operators

Membership operators check whether an element is present in a sequence.

### `in` and `not in`

```python
text = "Python is great"

"Python" in text      # True
"Java" in text        # False
"Java" not in text    # True
"python" in text      # False — case-sensitive
```

Works with lists, tuples and other sequences too (more on this in the data structures lesson):

```python
numbers = [1, 2, 3, 4, 5]
3 in numbers       # True
10 in numbers      # False
10 not in numbers  # True
```

---

## Logical operators

Logical operators combine boolean expressions.

### `and`, `or`, `not`

**`and`** — returns `True` only if **both** expressions are `True`:

```python
age = 25
has_licence = True

can_drive = age >= 18 and has_licence  # True
```

**`or`** — returns `True` if **at least one** expression is `True`:

```python
is_weekend = True
is_holiday = False

is_day_off = is_weekend or is_holiday  # True
```

**`not`** — inverts the boolean value:

```python
is_raining = False
good_weather = not is_raining  # True
```

### Combining logical operators

```python
age = 25
has_licence = True
has_car = False

can_travel = age >= 18 and (has_licence or has_car)  # True
```

Precedence of logical operators: `not` > `and` > `or`.

```python
True or False and False   # True  (and is evaluated first)
(True or False) and False # False (parentheses change the order)
```

When in doubt, use parentheses to make intent explicit.

### Short-circuit evaluation

Python does not evaluate expressions it does not need to:

- With `and`: if the first operand is `False`, the second is never evaluated.
- With `or`: if the first operand is `True`, the second is never evaluated.

```python
False and print("This never runs")  # nothing printed
True or print("This never runs")    # nothing printed
```

This is useful for safe guards:

```python
items = []

# ✅ Safe — items[0] is never accessed if items is empty
if len(items) > 0 and items[0] == 10:
    print("First item is 10")

# ❌ Unsafe — raises IndexError if items is empty
if items[0] == 10 and len(items) > 0:
    print("First item is 10")
```

### Logical operators return values, not just booleans

`and` and `or` return the actual value that determined the result, not just `True` or `False`:

```python
# and returns the first falsy value, or the last value if all are truthy
5 and 10     # 10
0 and 10     # 0
5 and 0      # 0

# or returns the first truthy value, or the last value if all are falsy
5 or 10      # 5
0 or 10      # 10
0 or False   # False
```

This is used in idiomatic Python for default values:

```python
name = user_input or "Anonymous"
```

---

## Operator precedence

When multiple operators appear in the same expression, Python evaluates them in this order (highest to lowest):

| Priority | Operator | Description |
|---|---|---|
| 1 | `**` | Exponentiation |
| 2 | `+x`, `-x` | Unary plus and minus |
| 3 | `*`, `/`, `//`, `%` | Multiplication, division |
| 4 | `+`, `-` | Addition, subtraction |
| 5 | `<`, `<=`, `>`, `>=`, `==`, `!=` | Comparison |
| 6 | `is`, `is not`, `in`, `not in` | Identity, membership |
| 7 | `not` | Logical NOT |
| 8 | `and` | Logical AND |
| 9 | `or` | Logical OR |

```python
2 + 3 * 4           # 14  (* before +)
5 < 10 and 3 > 1    # True (< and > before and)
not 5 > 3 or 2 < 1  # False
```

**Rule of thumb**: when in doubt, use parentheses. They make code more readable and eliminate ambiguity.

---

## Summary

- **Arithmetic**: `+`, `-`, `*`, `/`, `//`, `%`, `**`. Division `/` always returns a float.
- **String**: `+` concatenates, `*` repeats.
- **Assignment**: `=` assigns, `+=`, `-=`, etc. update in place.
- **Comparison**: `>`, `<`, `>=`, `<=`, `==`, `!=`. Always return a boolean.
- **Identity**: `is` / `is not` check object identity. Use `is` with `None`.
- **Membership**: `in` / `not in` check presence in a sequence.
- **Logical**: `and`, `or`, `not`. Short-circuit evaluation — Python skips what it does not need.
- Operator precedence determines evaluation order. Use parentheses to be explicit.

In the next lesson we will cover data structures — lists, tuples, dictionaries and sets.