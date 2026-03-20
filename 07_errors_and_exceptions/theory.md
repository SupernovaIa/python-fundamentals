# 07 — Errors and Exceptions

When programming, errors are inevitable. Python provides a robust system for handling them in a controlled way, allowing your program to continue running or make appropriate decisions when something goes wrong.

---

## Syntax errors vs exceptions

### Syntax errors

Syntax errors occur when your code does not follow Python's grammar rules. The interpreter cannot even start executing — it stops immediately and points to the problem:

```python
print("Hello world)   # SyntaxError: unterminated string
if True               # SyntaxError: expected ':'
    print("Hello")
```

- Cannot be caught with `try-except`.
- Must be fixed before the code can run at all.
- Python marks exactly where the problem is with `^`.

### Exceptions

Exceptions occur in syntactically correct code that encounters a problem at runtime:

```python
print(undefined_variable)  # NameError
result = 10 / 0             # ZeroDivisionError
number = int("text")        # ValueError
```

Unlike syntax errors, exceptions **can be anticipated and handled**, allowing your program to respond intelligently instead of crashing.

---

## try-except

The `try-except` block is the main mechanism for handling exceptions:

```python
try:
    # Code that might fail
    risky_code()
except SomeException:
    # Code that runs if that exception occurs
    handle_error()
```

### Execution flow

```python
print("1. Before try")

try:
    print("2. Inside try, before error")
    result = 10 / 0        # Error here
    print("3. Never reached")
except ZeroDivisionError:
    print("4. Handling the error")

print("5. After try-except")

# Output:
# 1. Before try
# 2. Inside try, before error
# 4. Handling the error
# 5. After try-except
```

When an exception occurs, the rest of the `try` block is skipped. Control jumps directly to the matching `except` block.

### Multiple except blocks

```python
try:
    age = int(input("Your age: "))
    result = 100 / age
    print(f"Result: {result}")
except ValueError:
    print("Error: enter a valid number")
except ZeroDivisionError:
    print("Error: age cannot be zero")
```

### Catching multiple exceptions in one block

```python
try:
    number = int(input("Number: "))
    result = 100 / number
except (ValueError, ZeroDivisionError):
    print("Invalid input or division by zero")
```

### Catching all exceptions

```python
# ❌ Avoid this — hides unexpected errors and catches KeyboardInterrupt
try:
    code()
except:
    print("An error occurred")

# ✅ Better — catches most errors but not system interrupts
try:
    code()
except Exception as e:
    print(f"Error: {e}")

# ✅ Best — be specific about what you expect
try:
    code()
except (ValueError, TypeError, KeyError) as e:
    print(f"Error: {e}")
```

Catching all exceptions blindly is bad practice — it hides bugs and makes debugging very hard.

### Accessing the exception object

Use `as` to capture the exception and inspect it:

```python
try:
    number = int("abc")
except ValueError as error:
    print(f"Type: {type(error)}")
    print(f"Message: {error}")

# Type: <class 'ValueError'>
# Message: invalid literal for int() with base 10: 'abc'
```

This is useful for logging errors or showing informative messages.

---

## Common exception types

| Exception | When it occurs |
|---|---|
| `TypeError` | Operation on an inappropriate type |
| `ValueError` | Right type, but inappropriate value |
| `IndexError` | List index out of range |
| `KeyError` | Dictionary key not found |
| `AttributeError` | Attribute or method does not exist |
| `FileNotFoundError` | File does not exist |
| `ZeroDivisionError` | Division by zero |
| `ImportError` / `ModuleNotFoundError` | Module cannot be imported |
| `NameError` | Variable not defined |
| `KeyboardInterrupt` | User pressed Ctrl+C |

### TypeError

```python
try:
    result = "5" + 5
except TypeError as e:
    print(f"Type error: {e}")
    result = int("5") + 5  # fix: convert first
```

### ValueError

```python
try:
    age = int(input("Your age: "))
except ValueError:
    print("Please enter a valid integer")
    age = None
```

### IndexError

```python
items = [1, 2, 3]
try:
    print(items[10])
except IndexError:
    print(f"Index out of range — list has {len(items)} elements")
```

### KeyError

```python
person = {"name": "Javi", "age": 29}
try:
    city = person["city"]
except KeyError:
    city = "Unknown"

# Better alternative — use get()
city = person.get("city", "Unknown")
```

### FileNotFoundError

```python
try:
    with open("data.txt", "r") as f:
        content = f.read()
except FileNotFoundError:
    print("File not found — creating empty file")
    with open("data.txt", "w") as f:
        f.write("")
```

### ImportError

```python
try:
    import numpy as np
except ImportError:
    print("NumPy is not installed. Run: pip install numpy")
    np = None
```

### KeyboardInterrupt

```python
try:
    while True:
        data = input("Enter something (Ctrl+C to quit): ")
        print(f"You entered: {data}")
except KeyboardInterrupt:
    print("\nProgram interrupted by user")
```

---

## raise

You can raise exceptions manually when you detect an invalid state in your code:

```python
raise ExceptionType("Descriptive error message")
```

### Input validation

```python
def calculate_average(scores):
    if not scores:
        raise ValueError("Score list cannot be empty")
    if any(s < 0 or s > 100 for s in scores):
        raise ValueError("Scores must be between 0 and 100")
    return sum(scores) / len(scores)

try:
    avg = calculate_average([])
except ValueError as e:
    print(f"Error: {e}")
# Error: Score list cannot be empty
```

### Type and value validation

```python
def create_user(name, age):
    if not name:
        raise ValueError("Name cannot be empty")
    if not isinstance(age, int):
        raise TypeError("Age must be an integer")
    if not 0 <= age <= 150:
        raise ValueError("Age must be between 0 and 150")
    return {"name": name, "age": age}
```

### Re-raising exceptions

Sometimes you want to handle an exception partially and then let it propagate:

```python
def load_config(path):
    try:
        with open(path) as f:
            return f.read()
    except FileNotFoundError:
        print(f"Config file not found: {path}")
        raise  # re-raise the original exception
```

---

## Custom exceptions

For domain-specific errors, create your own exception classes by inheriting from `Exception`:

```python
class InvalidAgeError(Exception):
    """Raised when an age value is outside the valid range."""
    pass

def verify_age(age):
    if age < 0:
        raise InvalidAgeError("Age cannot be negative")
    if age > 150:
        raise InvalidAgeError("Age cannot exceed 150")
    return True

try:
    verify_age(-5)
except InvalidAgeError as e:
    print(f"Error: {e}")
```

### Custom exception with extra data

```python
class InsufficientFundsError(Exception):
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        self.shortfall = amount - balance
        super().__init__(
            f"Insufficient funds. Balance: ${balance}, required: ${amount}"
        )

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError(self.balance, amount)
        self.balance -= amount

try:
    account = BankAccount(100)
    account.withdraw(150)
except InsufficientFundsError as e:
    print(e)
    print(f"Shortfall: ${e.shortfall}")
```

Custom exceptions are especially useful in AI engineering — for example, `ModelNotAvailableError`, `InvalidResponseError` or `RateLimitExceededError` make error handling much clearer than generic exceptions.

---

## else and finally

### else

The `else` block runs **only if no exception occurred** in the `try` block:

```python
try:
    number = int(input("Enter a number: "))
except ValueError:
    print("Invalid input")
else:
    # Only runs if no exception was raised
    print(f"Valid number: {number}")
    print(f"Double: {number * 2}")
```

The main use case for `else` is when the code inside it might raise different exceptions that you don't want the existing `except` blocks to catch.

### finally

The `finally` block **always runs**, regardless of whether an exception occurred:

```python
try:
    number = int(input("Number: "))
    result = 100 / number
except ValueError:
    print("Invalid input")
except ZeroDivisionError:
    print("Cannot divide by zero")
finally:
    print("This always runs")  # cleanup code goes here
```

`finally` runs even if there is a `return` in the `try` or `except` block:

```python
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None
    finally:
        print("finally runs before the function returns")

print(divide(10, 2))
# finally runs before the function returns
# 5.0
```

---

## Full structure: try-except-else-finally

```python
try:
    number = int(input("Number: "))
    result = 100 / number
except ValueError:
    print("Invalid input")
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print(f"Result: {result}")   # only if no exception
finally:
    print("End of block")        # always
```

**Execution order:**

1. `try` block runs.
2. If an exception occurs → matching `except` runs → `else` is skipped.
3. If no exception occurs → all `except` blocks are skipped → `else` runs.
4. `finally` **always** runs last.

---

## Context managers (with)

For managing resources like files and connections, the `with` statement is more Pythonic than `try-finally`. It guarantees cleanup automatically:

```python
# ❌ Manual approach — easy to forget to close
file = open("data.txt", "r")
try:
    content = file.read()
finally:
    file.close()

# ✅ Context manager — clean and safe
with open("data.txt", "r") as f:
    content = f.read()
# file is automatically closed here, even if an exception occurs
```

You will see `with` constantly in AI engineering — for file I/O, database connections, API sessions and more:

```python
# Multiple context managers
with open("input.txt") as infile, open("output.txt", "w") as outfile:
    for line in infile:
        outfile.write(line.upper())

# Database connection (example pattern)
with get_db_connection() as conn:
    results = conn.execute("SELECT * FROM users")
```

The `with` statement works with any object that implements the context manager protocol (`__enter__` and `__exit__`). You will learn how to create your own context managers in lesson `09_classes`.

---

## assert

`assert` verifies that a condition is `True`. If it is `False`, it raises `AssertionError`. Use it during development and testing to catch bugs early:

```python
assert condition, "Optional message if it fails"
```

```python
x = 10
assert x > 0           # passes silently
assert x < 0           # AssertionError

age = -5
assert age >= 0, "Age cannot be negative"
# AssertionError: Age cannot be negative
```

```python
def calculate_square_root(n):
    assert n >= 0, "Input must be non-negative"
    return n ** 0.5

def process_list(data):
    assert isinstance(data, list), "data must be a list"
    assert len(data) > 0, "list cannot be empty"
    return sum(data) / len(data)
```

> ⚠️ **Never use `assert` for production validation.** Python can be run with optimisations (`python -O`) that disable all `assert` statements. Use `raise` with explicit exception types for validation that must always run.

---

## Summary

**Core structure:**
- `try` — code that might fail.
- `except` — handle specific exceptions.
- `else` — runs only if no exception occurred.
- `finally` — always runs, used for cleanup.

**Raising exceptions:**
- `raise ExceptionType("message")` — signal an error condition.
- `raise` (alone) — re-raise the current exception.

**Custom exceptions:**
- Inherit from `Exception` for domain-specific errors.
- Add extra attributes when you need to carry more context.

**Context managers:**
- Use `with` instead of `try-finally` for managing resources.
- Cleaner, safer and more Pythonic.

**assert:**
- For debugging and development only — never for production validation.

**Best practices:**
- Be specific — catch the exceptions you expect, not everything.
- Never use bare `except:` — use `except Exception as e:` at minimum.
- Use `finally` or `with` to guarantee resource cleanup.
- Use custom exceptions to make domain errors explicit and meaningful.
- Do not use exceptions for normal control flow — they are for exceptional situations.

In the next lesson we will cover functions — how to organise and reuse your code.