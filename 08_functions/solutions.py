# 08 — Functions
# Solutions

import functools
import random

# ============================================================
# Exercise 1 — Basic functions and return
# ============================================================

def bmi(weight_kg: float, height_m: float) -> tuple[float, str]:
    """Compute BMI and return (value, category).

    Args:
        weight_kg: Weight in kilograms.
        height_m:  Height in metres.

    Raises:
        ValueError: If weight or height are <= 0.
    """
    if weight_kg <= 0 or height_m <= 0:
        raise ValueError("Weight and height must be greater than zero.")
    value = weight_kg / height_m ** 2
    if value < 18.5:
        category = "Underweight"
    elif value < 25:
        category = "Normal"
    elif value < 30:
        category = "Overweight"
    else:
        category = "Obese"
    return round(value, 1), category


for w, h in [(70, 1.75), (50, 1.75), (100, 1.75)]:
    print(bmi(w, h))

try:
    bmi(0, 1.75)
except ValueError as e:
    print(f"Error: {e}")


# ============================================================
# Exercise 2 — Default and keyword arguments
# ============================================================

SYMBOLS = {"EUR": "€", "USD": "$", "GBP": "£"}

def format_price(amount: float, currency: str = "EUR",
                 decimals: int = 2, show_symbol: bool = True) -> str:
    symbol = SYMBOLS.get(currency, currency)
    formatted = f"{amount:,.{decimals}f}"
    if show_symbol:
        return f"{symbol}{formatted}"
    return f"{formatted} {currency}"


print(format_price(1234.5))                        # €1,234.50
print(format_price(1234.5, currency="USD"))        # $1,234.50
print(format_price(1234.5, show_symbol=False))     # 1,234.50 EUR
print(format_price(1234.5, decimals=0))            # €1,235


# ============================================================
# Exercise 3 — Mutable default value bug
# ============================================================

# Buggy version (shared list across calls):
# def add_to_history(item, history=[]):
#     history.append(item)
#     return history

# Fixed version:
def add_to_history(item: str, history: list[str] | None = None,
                   allow_duplicates: bool = False) -> list[str]:
    if history is None:
        history = []
    if not allow_duplicates and item in history:
        return history
    history.append(item)
    return history


h1 = add_to_history("page1")
h2 = add_to_history("page2")
print(h1, h2)   # independent lists: ['page1']  ['page2']

shared: list[str] = []
add_to_history("page1", shared)
add_to_history("page1", shared)              # skipped: duplicate
add_to_history("page2", shared)
print(shared)                                # ['page1', 'page2']


# ============================================================
# Exercise 4 — *args and **kwargs
# ============================================================

def stats(*numbers: float) -> dict[str, float]:
    if not numbers:
        return {"count": 0, "sum": 0, "min": 0, "max": 0, "average": 0}
    return {
        "count": len(numbers),
        "sum": sum(numbers),
        "min": min(numbers),
        "max": max(numbers),
        "average": sum(numbers) / len(numbers),
    }


print(stats(4, 7, 2, 9, 1))
print(stats())


def build_profile(name: str, **attributes: object) -> dict[str, object]:
    return {"name": name, **attributes}


print(build_profile("Javi", age=29, role="AI Engineer"))


# ============================================================
# Exercise 5 — Scope and LEGB
# ============================================================

x = "global"

def outer() -> None:
    x = "enclosing"

    def inner() -> None:
        print(x)    # reads from enclosing scope → "enclosing"

    inner()


# Prediction Block A: prints "enclosing" then "global"
outer()
print(x)            # "global" (outer's x doesn't affect global)

# Block B:
total = 0

def add(n: int) -> int:
    total = total + n  # type: ignore[name-defined]  # UnboundLocalError!
    return total

# Prediction Block B: UnboundLocalError — Python sees an assignment to `total`
# inside the function so it treats it as local, but it's read before assignment.
try:
    print(add(5))
except Exception as e:
    print(f"Error: {e}")

# Block C:
def make_counter():
    count = 0

    def increment() -> int:
        nonlocal count
        count += 1
        return count

    return increment


# Prediction Block C: 1, 2, 3
counter = make_counter()
print(counter())    # 1
print(counter())    # 2
print(counter())    # 3


# ============================================================
# Exercise 6 — Lambda, map, filter
# ============================================================

orders = [
    {"product": "laptop", "price": 999.99},
    {"product": "mouse", "price": 29.99},
    {"product": "monitor", "price": 349.50},
    {"product": "keyboard", "price": 79.99},
    {"product": "usb hub", "price": 19.99},
    {"product": "headset", "price": 149.99},
]

# Pipeline: add VAT → filter > 100 → sort descending
result = sorted(
    filter(
        lambda o: o["final_price"] > 100,
        map(lambda o: {**o, "final_price": round(o["price"] * 1.21, 2)}, orders),
    ),
    key=lambda o: o["final_price"],
    reverse=True,
)

for o in result:
    print(f"{o['product']}: €{o['final_price']}")


# ============================================================
# Exercise 7 — Decorators
# ============================================================

# Part A: log_call decorator
def log_call(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"{func.__name__}({args}, {kwargs}) → {result}")
        return result
    return wrapper


@log_call
def add_numbers(a: int, b: int) -> int:
    return a + b


add_numbers(3, 4)


# Part B: retry decorator
def retry(times: int = 3):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last_exc: Exception | None = None
            for attempt in range(1, times + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exc = e
                    print(f"Attempt {attempt}/{times} failed: {e}")
            raise last_exc  # type: ignore[misc]
        return wrapper
    return decorator


@retry(times=3)
def flaky_operation() -> str:
    if random.random() < 0.6:
        raise RuntimeError("Random failure")
    return "Success"


try:
    print(flaky_operation())
except RuntimeError as e:
    print(f"All attempts failed: {e}")


# ============================================================
# Exercise 8 — Generators
# ============================================================

# Part A: infinite Fibonacci generator
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


fib = fibonacci()
print([next(fib) for _ in range(15)])


# Part B: read_in_chunks
def read_in_chunks(data: list, chunk_size: int):
    for i in range(0, len(data), chunk_size):
        yield data[i : i + chunk_size]


for chunk in read_in_chunks(list(range(1, 11)), 3):
    print(chunk)


# Part C: generator pipeline
numbers_gen = (n for n in range(1, 1001))
divisible_by_3 = (n for n in numbers_gen if n % 3 == 0)
squares = (n ** 2 for n in divisible_by_3)
print(sum(squares))
