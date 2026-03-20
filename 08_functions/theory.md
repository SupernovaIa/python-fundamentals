# 08 — Functions

Functions are reusable blocks of code with a name. They are one of the most important concepts in programming — they let you organise logic, avoid repetition and build systems from small, testable pieces.

---

## What is a function?

A function is a named block of code that:
- Has a **name** that identifies it.
- Can receive zero or more **arguments** as input.
- Executes a **sequence of instructions**.
- Can **return** a result.
- Can be **called** whenever needed.

**Why functions matter:**
- **Modularity** — break complex programs into small, manageable pieces.
- **Reusability** — write once, use many times.
- **Readability** — descriptive names make intent clear.
- **Maintainability** — fix a bug in one place, it is fixed everywhere.

---

## Defining functions

```python
def function_name(parameters):
    """Docstring — describes what the function does."""
    # function body
    return value  # optional
```

```python
def greet():
    print("Hello, world!")

greet()  # Hello, world!
```

> Parentheses `()` are required both in the definition and in the call, even with no parameters.

### return

`return` sends a value back to the caller and immediately stops the function:

```python
def add(a, b):
    return a + b

result = add(5, 3)  # 8
```

**Key behaviours:**

```python
# return stops execution immediately
def check_age(age):
    if age < 18:
        return "Minor"
    print("Only reached if age >= 18")
    return "Adult"

# return with no value returns None
def do_nothing():
    return

# No return statement also returns None
def greet(name):
    print(f"Hello, {name}")

result = greet("Ana")  # prints "Hello, Ana"
print(result)          # None
```

### Returning multiple values

Functions can return multiple values as a tuple:

```python
def calculate(a, b):
    return a + b, a - b, a * b

total, diff, product = calculate(10, 5)
print(total)    # 15
print(diff)     # 5
print(product)  # 50

# Or receive as a single tuple
results = calculate(10, 5)
print(results)  # (15, 5, 50)
```

### Docstrings

Docstrings document what a function does, what it expects and what it returns. Place them immediately after `def`, using triple quotes:

```python
def calculate_average(scores):
    """
    Calculate the average of a list of scores.

    Args:
        scores (list): A list of numeric scores.

    Returns:
        float: The average score.

    Raises:
        ValueError: If the list is empty.
    """
    if not scores:
        raise ValueError("Score list cannot be empty")
    return sum(scores) / len(scores)
```

Access the docstring programmatically:

```python
print(calculate_average.__doc__)
help(calculate_average)
```

---

## Arguments

### Positional arguments

Values are assigned to parameters by position — order matters:

```python
def introduce(name, age, city):
    print(f"My name is {name}, I am {age} and I live in {city}")

introduce("Javi", 29, "Madrid")  # ✅
introduce("Madrid", "Javi", 29)  # ❌ wrong order — confusing result
introduce("Javi", 29)            # ❌ TypeError: missing argument
```

### Keyword arguments

Specify which parameter each value goes to — order no longer matters:

```python
introduce(city="Madrid", name="Javi", age=29)  # ✅
```

### Mixing positional and keyword

Positional arguments must always come first:

```python
introduce("Javi", age=29, city="Madrid")  # ✅
introduce(name="Javi", 29, city="Madrid") # ❌ SyntaxError
```

### Default parameters

Provide fallback values for parameters. If the caller does not pass a value, the default is used:

```python
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Ana")               # Hello, Ana!
greet("Ana", "Good morning") # Good morning, Ana!
```

Parameters with defaults must come **after** parameters without defaults:

```python
def function(a, b, c=0, d=1):  # ✅
    pass

def function(a, b=0, c, d=1):  # ❌ SyntaxError
    pass
```

### ⚠️ Mutable default values

Never use mutable objects (lists, dicts) as default values — the object is created once when the function is defined, not on each call:

```python
# ❌ Bug — the list persists between calls
def add_item(item, items=[]):
    items.append(item)
    return items

print(add_item(1))  # [1]
print(add_item(2))  # [1, 2] — unexpected!
print(add_item(3))  # [1, 2, 3] — the list keeps growing

# ✅ Use None as default, create the object inside
def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items

print(add_item(1))  # [1]
print(add_item(2))  # [2] — correct
```

---

## *args and **kwargs

These allow functions to accept a variable number of arguments.

### *args — variable positional arguments

`*args` collects any number of positional arguments into a **tuple**:

```python
def add(*args):
    return sum(args)

add(1, 2, 3)        # 6
add(1, 2, 3, 4, 5)  # 15
add(10)             # 10
add()               # 0
```

### **kwargs — variable keyword arguments

`**kwargs` collects any number of keyword arguments into a **dict**:

```python
def show_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

show_info(name="Javi", age=29, city="Madrid")
# name: Javi
# age: 29
# city: Madrid
```

### Combining all argument types

The required order is: positional → *args → keyword-only → **kwargs:

```python
def function(normal_arg, *args, keyword_arg="default", **kwargs):
    print(f"Normal: {normal_arg}")
    print(f"Args: {args}")
    print(f"Keyword: {keyword_arg}")
    print(f"Kwargs: {kwargs}")

function(1, 2, 3, keyword_arg="custom", extra1="a", extra2="b")
# Normal: 1
# Args: (2, 3)
# Keyword: custom
# Kwargs: {'extra1': 'a', 'extra2': 'b'}
```

### Unpacking with * and **

You can also use `*` and `**` when calling a function to unpack iterables and dicts:

```python
def add(a, b, c):
    return a + b + c

numbers = [1, 2, 3]
add(*numbers)  # equivalent to add(1, 2, 3)

params = {"a": 1, "b": 2, "c": 3}
add(**params)  # equivalent to add(a=1, b=2, c=3)
```

---

## Scope and the LEGB rule

**Scope** determines where a variable is visible. Python searches for names in this order:

1. **L**ocal — inside the current function.
2. **E**nclosing — in any enclosing functions (for nested functions).
3. **G**lobal — at the top level of the module.
4. **B**uilt-in — Python's predefined names (`print`, `len`, etc.).

```python
x = "global"

def outer():
    x = "enclosing"

    def inner():
        x = "local"
        print(x)  # "local"

    inner()

outer()
print(x)  # "global"
```

### global and nonlocal

By default you can read outer variables but not reassign them. Use `global` or `nonlocal` to modify them — but this is generally considered bad practice:

```python
# ❌ Avoid global state
counter = 0
def increment():
    global counter
    counter += 1

# ✅ Better — pass as argument, return the result
def increment(counter):
    return counter + 1

counter = 0
counter = increment(counter)
```

`nonlocal` works the same way for enclosing (not global) scope in nested functions. Both `global` and `nonlocal` break function isolation and make code harder to reason about — prefer passing arguments and returning values.

---

## Lambda functions

Lambda functions are anonymous, single-expression functions:

```python
lambda arguments: expression
```

```python
square = lambda x: x ** 2
square(5)  # 25

add = lambda a, b: a + b
add(3, 5)  # 8
```

**Primary use case — as inline arguments to higher-order functions:**

```python
people = [
    {"name": "Ana", "age": 25},
    {"name": "Juan", "age": 30},
    {"name": "María", "age": 22}
]

people.sort(key=lambda p: p["age"])
# [{"name": "María", ...}, {"name": "Ana", ...}, {"name": "Juan", ...}]
```

**When to use lambda:**
- ✅ Simple single-expression operations passed as arguments.
- ✅ `sorted`, `map`, `filter`, `key=` parameters.
- ❌ Complex logic — use a named function instead.
- ❌ Functions you need to reuse or test independently.

---

## map, filter, reduce

Higher-order functions that apply operations to iterables.

### map()

Applies a function to every element of an iterable:

```python
numbers = [1, 2, 3, 4, 5]

squares = list(map(lambda x: x ** 2, numbers))
# [1, 4, 9, 16, 25]

# Converting types
strings = ["1", "2", "3"]
integers = list(map(int, strings))
# [1, 2, 3]

# Multiple iterables
a = [1, 2, 3]
b = [4, 5, 6]
sums = list(map(lambda x, y: x + y, a, b))
# [5, 7, 9]
```

### filter()

Keeps only elements for which the function returns `True`:

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8]

evens = list(filter(lambda x: x % 2 == 0, numbers))
# [2, 4, 6, 8]

# filter(None, iterable) removes falsy values
texts = ["hello", "", "world", "", "python"]
non_empty = list(filter(None, texts))
# ['hello', 'world', 'python']
```

### reduce()

Reduces an iterable to a single value by applying a function cumulatively:

```python
from functools import reduce

numbers = [1, 2, 3, 4, 5]

total = reduce(lambda x, y: x + y, numbers)     # 15
product = reduce(lambda x, y: x * y, numbers)   # 120
maximum = reduce(lambda x, y: x if x > y else y, numbers)  # 5

# With an initial value
reduce(lambda x, y: x + y, [1, 2, 3], 10)  # 16
```

> In most cases, comprehensions are more readable than `map` and `filter`, and built-ins like `sum()`, `max()`, `min()` are clearer than `reduce()`. Use these functional tools when you need to compose pipelines or work with functions as first-class objects.

---

## Decorators

Decorators are functions that wrap other functions to extend or modify their behaviour — without changing the original function's code.

### The concept

```python
def my_decorator(func):
    def wrapper():
        print("Before")
        func()
        print("After")
    return wrapper

def greet():
    print("Hello!")

greet = my_decorator(greet)
greet()
# Before
# Hello!
# After
```

### The @ syntax

Python provides cleaner syntax for applying decorators:

```python
def my_decorator(func):
    def wrapper():
        print("Before")
        func()
        print("After")
    return wrapper

@my_decorator
def greet():
    print("Hello!")

greet()
# Before
# Hello!
# After
```

### Decorators with arguments — use *args and **kwargs

To decorate functions that accept arguments:

```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Result: {result}")
        return result
    return wrapper

@my_decorator
def add(a, b):
    return a + b

add(5, 3)
# Calling add
# Result: 8
```

### functools.wraps

Always use `@functools.wraps(func)` on the wrapper — it preserves the original function's name, docstring and metadata:

```python
import functools

def my_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("Before")
        result = func(*args, **kwargs)
        print("After")
        return result
    return wrapper

@my_decorator
def add(a, b):
    """Adds two numbers."""
    return a + b

print(add.__name__)  # "add" — not "wrapper"
print(add.__doc__)   # "Adds two numbers."
```

### Practical example — timing

```python
import time
import functools

def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start
        print(f"{func.__name__} took {elapsed:.4f}s")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(1)

slow_function()
# slow_function took 1.0003s
```

### Decorators with parameters

Add an extra outer function to pass parameters to the decorator:

```python
def repeat(times):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    print(f"Hello, {name}!")

greet("Ana")
# Hello, Ana!
# Hello, Ana!
# Hello, Ana!
```

### Stacking decorators

Multiple decorators are applied bottom-up:

```python
@decorator_a
@decorator_b
def function():
    pass

# Equivalent to: function = decorator_a(decorator_b(function))
```

Decorators are used extensively in AI engineering frameworks — FastAPI uses them for route definitions, LangChain for chain steps, and many observability tools for tracing.

---

## Generators

Generators are functions that produce values one at a time, on demand, instead of building the entire sequence in memory. They use `yield` instead of `return`.

### yield vs return

- `return` terminates the function and sends a value back.
- `yield` pauses the function, sends a value, and resumes from the same point on the next call.

```python
def my_generator():
    yield 1
    yield 2
    yield 3

gen = my_generator()

next(gen)  # 1
next(gen)  # 2
next(gen)  # 3
next(gen)  # StopIteration
```

### List vs generator — the key difference

```python
# List — builds everything in memory immediately
def squares_list(n):
    return [i ** 2 for i in range(n)]

# Generator — produces one value at a time, on demand
def squares_gen(n):
    for i in range(n):
        yield i ** 2

# For 1 million items:
squares_list(1_000_000)  # allocates memory for 1M integers
squares_gen(1_000_000)   # allocates memory for one integer at a time
```

### Iterating over a generator

```python
for square in squares_gen(5):
    print(square)
# 0, 1, 4, 9, 16

# Works with all iterable-consuming functions
total = sum(squares_gen(5))  # 30
```

### Generator expressions (recap)

Covered in lesson `06_control_flow` — use parentheses instead of brackets:

```python
squares = (x ** 2 for x in range(10))  # generator, not a list
total = sum(x ** 2 for x in range(10)) # no extra parentheses needed
```

### yield from

Delegates to another generator or iterable:

```python
def generator_a():
    yield 1
    yield 2

def generator_b():
    yield 3
    yield 4

def combined():
    yield from generator_a()
    yield from generator_b()

list(combined())  # [1, 2, 3, 4]
```

### Sending values with send()

Generators can receive values mid-execution:

```python
def accumulator():
    total = 0
    while True:
        value = yield total
        if value is None:
            break
        total += value

gen = accumulator()
next(gen)        # initialise — returns 0
gen.send(10)     # returns 10
gen.send(20)     # returns 30
gen.send(5)      # returns 35
```

### When to use generators

✅ Use generators when:
- Working with large datasets that would not fit in memory.
- Processing streams of data (files, API responses, log lines).
- You only need to iterate once.
- Building lazy pipelines.

❌ Avoid generators when:
- You need to access elements by index.
- You need to iterate multiple times.
- You need to know the total length upfront.

| | List | Generator |
|---|---|---|
| Memory | All values at once | One at a time |
| Reusable | ✅ | ❌ (exhausted after one pass) |
| Indexable | ✅ | ❌ |
| `len()` | ✅ | ❌ |

---

## Summary

**Core concepts:**
- Define with `def`, call with `()`, return values with `return`.
- Document with docstrings (`Args`, `Returns`, `Raises`).
- Never use mutable objects as default parameter values — use `None`.

**Arguments:**
- Positional — order matters.
- Keyword — order does not matter.
- Default — fallback values for optional parameters.
- `*args` — variable positional, received as tuple.
- `**kwargs` — variable keyword, received as dict.

**Scope:**
- LEGB: Local → Enclosing → Global → Built-in.
- Avoid `global` and `nonlocal` — prefer passing arguments and returning values.

**Functional tools:**
- `lambda` — anonymous single-expression functions, best as inline arguments.
- `map()` / `filter()` — apply or select from iterables.
- `reduce()` — fold an iterable to a single value.
- Comprehensions are usually more readable than `map`/`filter`.

**Decorators:**
- Wrap functions to add behaviour without modifying them.
- Always use `@functools.wraps(func)` to preserve metadata.
- Used extensively in FastAPI, LangChain and observability tools.

**Generators:**
- Use `yield` to produce values lazily, one at a time.
- Essential for large datasets and streaming pipelines.
- Generator expressions `(x for x in ...)` are the concise form.

**Best practices:**
- One function, one responsibility.
- Descriptive names in `snake_case`.
- Keep functions short — if it does not fit on a screen, consider splitting it.
- Prefer immutable defaults.
- Use generators for large data — never load a million rows into a list unnecessarily.

In the next lesson we will cover classes and object-oriented programming.