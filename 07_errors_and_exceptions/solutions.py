# 07 — Errors and Exceptions
# Solutions

# ============================================================
# Exercise 1 — Basic try-except
# ============================================================

def safe_divide(a_str: str, b_str: str) -> float | None:
    try:
        a = float(a_str)
        b = float(b_str)
        return a / b
    except ValueError:
        print(f"Invalid input: '{a_str}' or '{b_str}' cannot be converted to float.")
        return None
    except ZeroDivisionError:
        print("Error: division by zero.")
        return None


print(safe_divide("10", "2"))    # 5.0
print(safe_divide("abc", "2"))   # error message, None
print(safe_divide("10", "0"))    # error message, None


# ============================================================
# Exercise 2 — Multiple exceptions and execution flow
# ============================================================

# Block A:
# Prediction: int("42") succeeds → x=42, then 42/0 → ZeroDivisionError
#             prints "A: ZeroDivisionError" then "A: finally"
try:
    x = int("42")
    y = x / 0
    print("A: success")
except ValueError:
    print("A: ValueError")
except ZeroDivisionError:
    print("A: ZeroDivisionError")   # ← this runs
finally:
    print("A: finally")             # ← always runs

# Block B:
# Prediction: items[1]=2 succeeds → no exception → else runs, then finally
try:
    items = [1, 2, 3]
    print(items[1])             # 2
except IndexError:
    print("B: IndexError")
else:
    print("B: else")            # ← no exception, else runs
finally:
    print("B: finally")         # ← always runs

# Block C:
# Prediction: data["missing"] raises KeyError → prints key with quotes
try:
    data = {"key": "value"}
    print(data["missing"])
except KeyError as e:
    print(f"C: KeyError — {e}")         # 'missing'
except Exception as e:
    print(f"C: Exception — {e}")


# ============================================================
# Exercise 3 — Input validation with raise
# ============================================================

def register_user(name: str, age: int, email: str) -> dict:
    if not name or not name.strip():
        raise ValueError("Name cannot be empty.")
    if not isinstance(age, int):
        raise TypeError(f"Age must be an integer, got {type(age).__name__}.")
    if not 0 <= age <= 120:
        raise ValueError(f"Age must be between 0 and 120, got {age}.")
    if "@" not in email:
        raise ValueError(f"Invalid email address: '{email}'.")
    return {"name": name.strip(), "age": age, "email": email}


# Test valid input
try:
    user = register_user("Javi", 29, "javi@example.com")
    print(user)
except (ValueError, TypeError) as e:
    print(f"Error: {e}")

# Test invalid inputs
for args in [
    ("", 29, "javi@example.com"),
    ("Javi", "29", "javi@example.com"),
    ("Javi", 150, "javi@example.com"),
    ("Javi", 29, "not-an-email"),
]:
    try:
        register_user(*args)  # type: ignore[arg-type]
    except (ValueError, TypeError) as e:
        print(f"Caught: {e}")


# ============================================================
# Exercise 4 — Custom exceptions
# ============================================================

class APIError(Exception):
    """Base class for API errors."""


class RateLimitError(APIError):
    def __init__(self, retry_after: int) -> None:
        self.retry_after = retry_after
        super().__init__(f"Rate limit exceeded. Retry after {retry_after}s.")


class InvalidResponseError(APIError):
    def __init__(self, status_code: int) -> None:
        self.status_code = status_code
        super().__init__(f"Invalid response: HTTP {status_code}.")


def simulate_api_call(status_code: int) -> str:
    if status_code == 200:
        return "OK"
    if status_code == 429:
        raise RateLimitError(retry_after=60)
    raise InvalidResponseError(status_code)


for code in [200, 429, 500]:
    try:
        result = simulate_api_call(code)
        print(f"Success: {result}")
    except RateLimitError as e:
        print(f"Rate limited — retry in {e.retry_after}s")
    except InvalidResponseError as e:
        print(f"Bad response — status {e.status_code}")


# ============================================================
# Exercise 5 — Context managers
# ============================================================

# Part A: write using a context manager
with open("sample.txt", "w") as f:
    f.write("Hello from Python\n")
    f.write("Second line\n")

# Part B: read back with line numbers
with open("sample.txt") as f:
    for i, line in enumerate(f, start=1):
        print(f"{i}: {line}", end="")


# ============================================================
# Exercise 6 — Robust data processing
# ============================================================

raw_records = [
    {"product": "laptop", "price": "999.99", "quantity": "5"},
    {"product": "mouse", "price": "abc", "quantity": "10"},
    {"product": "monitor", "price": "349.50", "quantity": "0"},
    {"product": "keyboard", "price": "79.99", "quantity": "3"},
    {"product": "headset", "price": "-1", "quantity": "2"},
    {"product": "webcam", "price": "89.99", "quantity": "7"},
]

valid_records = []

for record in raw_records:
    try:
        price = float(record["price"])
        quantity = int(record["quantity"])
    except ValueError:
        print(f"Skipping '{record['product']}': conversion error.")
        continue

    if price <= 0 or quantity <= 0:
        print(f"Skipping '{record['product']}': invalid price or quantity.")
        continue

    total = price * quantity
    valid_records.append({**record, "price": price, "quantity": quantity, "total": total})

print(f"\nValid records: {len(valid_records)}")
for r in valid_records:
    print(f"  {r['product']}: {r['quantity']} × €{r['price']:.2f} = €{r['total']:.2f}")


# ============================================================
# Exercise 7 — assert
# ============================================================

def matrix_multiply(a: list[list[float]], b: list[list[float]]) -> list[list[float]]:
    assert a and isinstance(a, list), "a must be a non-empty list."
    assert b and isinstance(b, list), "b must be a non-empty list."
    row_len_a = len(a[0])
    assert all(len(row) == row_len_a for row in a), "All rows in a must have equal length."
    row_len_b = len(b[0])
    assert all(len(row) == row_len_b for row in b), "All rows in b must have equal length."
    assert row_len_a == len(b), "Columns of a must equal rows of b."

    rows_a, cols_b, cols_a = len(a), len(b[0]), len(a[0])
    result = [[0.0] * cols_b for _ in range(rows_a)]
    for i in range(rows_a):
        for j in range(cols_b):
            for k in range(cols_a):
                result[i][j] += a[i][k] * b[k][j]
    return result


# Valid inputs
a = [[1, 2], [3, 4]]
b = [[5, 6], [7, 8]]
print(matrix_multiply(a, b))   # [[19.0, 22.0], [43.0, 50.0]]

# Invalid: incompatible dimensions
try:
    matrix_multiply([[1, 2, 3]], [[1, 2], [3, 4]])
except AssertionError as e:
    print(f"AssertionError: {e}")
