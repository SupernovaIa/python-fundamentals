# 10 — Modular Programming

Modular programming is the practice of dividing large programs into smaller, manageable pieces called **modules**. Instead of writing everything in one giant file, you organise code into logical components that can be developed, tested and maintained independently.

**Benefits:**
- **Simplicity** — each module focuses on one part of the problem.
- **Maintainability** — modify one module without breaking others.
- **Reusability** — use the same module across multiple projects.
- **Namespace isolation** — avoid name conflicts between different parts of the codebase.

---

## Modules

A **module** is a `.py` file containing Python code — functions, classes, variables. Any `.py` file is automatically a module.

### Creating a module

```python
# file: math_utils.py

PI = 3.14159

def add(a, b):
    """Add two numbers."""
    return a + b

def subtract(a, b):
    """Subtract b from a."""
    return a - b

def circle_area(radius):
    """Calculate the area of a circle."""
    return PI * radius ** 2

class Calculator:
    def multiply(self, a, b):
        return a * b
```

### Importing a module

```python
import math_utils

print(math_utils.PI)               # 3.14159
result = math_utils.add(5, 3)      # 8
area = math_utils.circle_area(10)
```

### Importing specific names

```python
from math_utils import add, PI

print(PI)        # 3.14159
add(10, 5)       # 15

# circle_area is not available — not imported
```

### Aliases

```python
import math_utils as mu
mu.add(1, 2)

from math_utils import circle_area as area
area(10)

# Community conventions you will see constantly
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
```

### Avoid import *

```python
# ❌ Avoid — pollutes namespace, hides where names come from
from math_utils import *

# ✅ Be explicit
from math_utils import add, subtract, PI
```

---

## Module search path

When you run `import my_module`, Python searches in this order:

1. The current directory (where the script runs).
2. Directories in the `PYTHONPATH` environment variable.
3. Installation directories (where packages are installed).

```python
import sys
print(sys.path)  # shows the full search path
```

> Avoid modifying `sys.path` manually in production code. Install your project properly instead (covered below).

---

## __name__ and __main__

`__name__` is a special variable that tells you how a module is being used:

- **Run directly** → `__name__ == '__main__'`
- **Imported** → `__name__` equals the module's filename (without `.py`)

```python
# file: calculations.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

if __name__ == '__main__':
    # Only runs when the file is executed directly
    # Does NOT run when imported
    print("Testing calculations module...")
    assert add(5, 3) == 8
    assert subtract(10, 4) == 6
    print("All tests passed")
```

```bash
python calculations.py   # runs the test block
```

```python
import calculations      # test block does NOT run
calculations.add(1, 2)   # 3
```

### Common use cases

**Script that is also importable:**

```python
# file: validate.py

def is_valid_email(email):
    return "@" in email and "." in email.split("@")[-1]

def is_valid_url(url):
    return url.startswith(("http://", "https://"))

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        email = sys.argv[1]
        status = "valid" if is_valid_email(email) else "invalid"
        print(f"{email} is {status}")
    else:
        print("Usage: python validate.py email@example.com")
```

```bash
python validate.py user@example.com   # valid
```

```python
from validate import is_valid_email   # import without side effects
```

---

## Packages

A **package** is a directory that contains an `__init__.py` file and one or more modules. Packages let you organise related modules into a hierarchy.

### Typical package structure

```
my_project/
├── pyproject.toml
└── my_package/
    ├── __init__.py
    ├── utils.py
    ├── models.py
    └── api/
        ├── __init__.py
        ├── client.py
        └── auth.py
```

### __init__.py

This file marks a directory as a package. It can be empty, or it can contain initialisation code and re-exports:

```python
# my_package/__init__.py

# Option 1 — empty (minimal, always works)

# Option 2 — expose a clean public API
from .utils import clean_text, validate_email
from .models import User, Product

VERSION = "1.0.0"
```

With Option 2, users can do:

```python
from my_package import User, clean_text
# instead of
from my_package.models import User
from my_package.utils import clean_text
```

### __all__

`__all__` controls what gets exported when someone does `from package import *`. It also documents the public API:

```python
# my_package/__init__.py

__all__ = ["User", "Product", "clean_text"]

from .models import User, Product
from .utils import clean_text
```

```python
from my_package import *   # imports only what's in __all__
```

### Importing from packages

```python
# Import a module from a package
import my_package.utils
my_package.utils.clean_text("  hello  ")

# Import a specific name from a submodule
from my_package.utils import clean_text
clean_text("  hello  ")

# Import from a subpackage
from my_package.api.client import APIClient
```

---

## Absolute vs relative imports

### Absolute imports

Use the full path from the project root. **Always prefer these.**

```python
from my_package.utils import clean_text
from my_package.api.client import APIClient
```

They work from anywhere, are explicit and easy to follow.

### Relative imports

Use `.` and `..` to refer to the current and parent package. Only valid inside a package — not in scripts run directly.

```python
# inside my_package/models.py
from .utils import clean_text          # same package
from ..config import settings          # parent package
```

```
.   = current package directory
..  = parent package directory
```

**When to use relative imports:**
- Inside a large, well-structured package.
- When the package may be renamed (internal paths stay valid).

**Use absolute imports everywhere else** — they are clearer and less error-prone.

### Circular imports

A circular import happens when module A imports from B and B imports from A. Python partially initialises one of them, leading to `ImportError` or missing names.

```python
# ❌ Circular — a.py imports b, b.py imports a
# a.py
from b import func_b

# b.py
from a import func_a  # ImportError or NameError
```

**Solutions:**
1. Restructure — move shared code to a third module `common.py`.
2. Defer the import — move it inside the function that needs it:

```python
# b.py
def func_b():
    from a import func_a  # imported only when func_b() is called
    return func_a()
```

---

## Installing in development mode

To use absolute imports reliably across your project, install it as a package in editable (development) mode. This avoids `sys.path` hacks.

### pyproject.toml

Create this file at the project root:

```toml
[build-system]
requires = ["setuptools>=61.0"]
build-backend = "setuptools.build_meta"

[project]
name = "my_package"
version = "0.1.0"
description = "My Python project"
requires-python = ">=3.10"
dependencies = [
    "requests>=2.28",
]

[project.optional-dependencies]
dev = [
    "pytest>=7.0",
    "ruff>=0.1",
]
```

### Installing with pip

```bash
pip install -e .
```

### Installing with uv (recommended)

We cover `uv` in depth in lesson `14_dependency_management`. The short version:

```bash
uv sync          # install all dependencies
uv pip install -e .  # install project in editable mode
```

Once installed, absolute imports work from anywhere in the project:

```python
# works from any script, any directory
from my_package.utils import clean_text
```

---

## Useful standard library modules

Python ships with a rich standard library. These are the modules you will reach for most often:

```python
# File system paths — prefer pathlib over os.path
from pathlib import Path

p = Path("data/file.txt")
p.exists()           # True/False
p.parent             # Path("data")
p.stem               # "file"
p.suffix             # ".txt"
p.read_text()        # read file contents
p.write_text("hi")  # write to file

files = list(Path(".").glob("*.py"))  # all .py files in current dir
```

```python
# OS and environment
import os

os.getcwd()                   # current working directory
os.environ.get("API_KEY")     # read env variable safely
os.makedirs("output", exist_ok=True)  # create directory
```

```python
# JSON
import json

data = {"name": "Javi", "age": 29}
json_str = json.dumps(data, indent=2)   # dict → string
data_back = json.loads(json_str)        # string → dict

# Read/write JSON files
with open("data.json", "w") as f:
    json.dump(data, f, indent=2)

with open("data.json") as f:
    data = json.load(f)
```

```python
# Date and time
from datetime import datetime, timedelta

now = datetime.now()
print(now.strftime("%Y-%m-%d %H:%M:%S"))   # "2026-01-15 09:30:00"
yesterday = now - timedelta(days=1)
```

```python
# Regular expressions
import re

text = "Contact us at support@example.com or sales@example.com"
emails = re.findall(r"[\w.+-]+@[\w-]+\.[a-z]+", text)
# ['support@example.com', 'sales@example.com']

re.sub(r"\s+", " ", "too   many    spaces")  # "too many spaces"
```

```python
# Random
import random

random.randint(1, 10)          # integer between 1 and 10
random.choice(["a", "b", "c"]) # random element
random.shuffle(my_list)        # shuffle in place
random.sample(my_list, k=3)    # 3 unique random elements
```

```python
# Math
import math

math.sqrt(16)     # 4.0
math.floor(3.7)   # 3
math.ceil(3.2)    # 4
math.log(100, 10) # 2.0
math.pi           # 3.141592653589793
```

```python
# Collections — useful data structures
from collections import Counter, defaultdict, deque

# Counter — count occurrences
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
counts = Counter(words)
counts.most_common(2)   # [('apple', 3), ('banana', 2)]

# defaultdict — dict with a default value for missing keys
from collections import defaultdict
grouped = defaultdict(list)
for word in words:
    grouped[word[0]].append(word)   # group by first letter

# deque — efficient append/pop from both ends
dq = deque([1, 2, 3])
dq.appendleft(0)   # [0, 1, 2, 3]
dq.popleft()       # 0
```

```python
# itertools — tools for working with iterables
import itertools

list(itertools.chain([1, 2], [3, 4], [5]))  # [1, 2, 3, 4, 5]
list(itertools.islice(range(100), 5))        # [0, 1, 2, 3, 4]
list(itertools.combinations([1, 2, 3], 2))  # [(1,2),(1,3),(2,3)]
list(itertools.product([0, 1], repeat=3))   # all 3-bit combinations
```

```python
# functools — higher-order function tools
from functools import lru_cache, partial, reduce

# Cache results of expensive function calls
@lru_cache(maxsize=128)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# Partial application — fix some arguments
from functools import partial
def power(base, exp):
    return base ** exp

square = partial(power, exp=2)
cube = partial(power, exp=3)
square(5)   # 25
cube(3)     # 27
```

---

## Named tuples

We promised in lesson `04_data_structures` to cover named tuples here. They are part of `collections` and combine tuple immutability with readable attribute access.

```python
from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])
p = Point(10, 20)

print(p.x)     # 10 — attribute access
print(p[0])    # 10 — index access still works
print(p)       # Point(x=10, y=20) — clean repr

# Immutable — cannot be modified
p.x = 5        # AttributeError
```

Named tuples are lightweight and memory-efficient — good for returning structured data from functions when a full class is overkill:

```python
ModelResult = namedtuple("ModelResult", ["response", "tokens", "latency_ms"])

def call_model(prompt):
    # ... call the model ...
    return ModelResult(
        response="The answer is 42",
        tokens=150,
        latency_ms=320.5
    )

result = call_model("What is the answer?")
print(result.response)     # "The answer is 42"
print(result.latency_ms)   # 320.5
```

For more complex cases with defaults and type annotations, prefer `@dataclass` (covered in lesson `09_classes`).

---

## Best practices

**Import order** — follow PEP 8:

```python
# 1. Standard library
import os
import sys
from datetime import datetime
from pathlib import Path

# 2. Third-party
import numpy as np
import pandas as pd

# 3. Local modules
from my_package import utils
from my_package.models import User
```

**Module naming** — lowercase with underscores, short and descriptive:

```python
# ✅
math_utils.py
data_loader.py
api_client.py

# ❌
String.py      # conflicts with stdlib
test.py        # too generic
MyModule.py    # PascalCase not for modules
```

**Document your modules:**

```python
"""
Math utilities for the AI engineering pipeline.

Provides functions for numerical operations, statistical
calculations and data normalisation.

Example:
    from my_package.math_utils import normalise
    values = normalise([1, 2, 3, 4, 5])
"""
```

**Use `if __name__ == '__main__'`** for code that should only run when the file is executed directly.

**Avoid circular imports** — restructure code or use local imports as a last resort.

**Install with `pip install -e .`** (or `uv sync`) — never rely on `sys.path` manipulation in real projects.

---

## Summary

- A **module** is any `.py` file. Import it with `import` or `from ... import`.
- A **package** is a directory with `__init__.py`. Use it to group related modules.
- **Absolute imports** — always prefer them: `from my_package.utils import clean_text`.
- **Relative imports** — use only inside packages: `from .utils import clean_text`.
- **`__name__`** — use `if __name__ == '__main__':` to separate script code from importable code.
- **`__init__.py`** — controls the package's public API. Use `__all__` to be explicit.
- **`pyproject.toml` + `pip install -e .`** — the standard way to make your package importable without `sys.path` hacks.
- **Named tuples** — lightweight immutable records from `collections.namedtuple`.
- Import order: standard library → third-party → local.

In the next lesson we will cover file handling — reading, writing and managing files in Python.