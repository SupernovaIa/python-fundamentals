# 13 — Code Formatting with Ruff

Writing code that works is only half the job. Code that is consistent, readable and free of common mistakes is what separates professional projects from hobby scripts. Ruff automates this entirely.

---

## What is Ruff?

Ruff is a Python linter and formatter written in Rust — which makes it 10–100× faster than traditional tools. It replaces an entire toolchain with a single binary:

| What it replaces | What Ruff does |
|---|---|
| Black | Formatting |
| isort | Import sorting |
| Flake8 | Style linting |
| Pylint | Additional linting |
| pyupgrade | Modernise syntax |
| bandit | Security checks |

**Three things Ruff does:**
- **Linting** — finds problems, bad practices and style violations.
- **Formatting** — rewrites your code to a consistent style automatically.
- **Import sorting** — groups and orders imports following PEP 8.

---

## Installation

### VS Code extension

1. Open VS Code.
2. Press `Ctrl+Shift+X` (Windows/Linux) or `Cmd+Shift+X` (Mac).
3. Search for **"Ruff"** and install the extension by **Astral**.

### CLI with uv (recommended)

We cover `uv` fully in lesson `14_dependency_management`. The short version:

```bash
# Install ruff as a dev dependency in your project
uv add --dev ruff

# Or install it globally as a tool
uv tool install ruff
```

```bash
# Verify installation
ruff --version
```

---

## Format on save

Enable automatic formatting every time you save a file:

1. Open Settings (`Cmd+,` on Mac / `Ctrl+,` on Windows).
2. Search **"format on save"** → enable **Editor: Format On Save**.
3. Search **"default formatter"** → set **Editor: Default Formatter** to **Ruff**.

From now on, every `Cmd+S` / `Ctrl+S` triggers Ruff automatically.

If auto-format does not work: right-click inside a Python file → **Format Document**. Or use the shortcut `Shift+Alt+F` (Windows/Linux) / `Shift+Option+F` (Mac).

---

## What Ruff fixes automatically

Here is a real example of what Ruff does on save:

**Before — unformatted:**

```python
import os
def   calculate_total(items):
    total=0
    for item in items:
        total+=item['price']*item['quantity']
    return total
shopping_cart=[{'name':'apple','price':0.5,'quantity':6},{'name':'banana','price':0.3,'quantity':8}]
print(calculate_total(shopping_cart))
```

**After — Ruff formats on save:**

```python
import os


def calculate_total(items):
    total = 0
    for item in items:
        total += item["price"] * item["quantity"]
    return total


shopping_cart = [
    {"name": "apple", "price": 0.5, "quantity": 6},
    {"name": "banana", "price": 0.3, "quantity": 8},
]
print(calculate_total(shopping_cart))
```

**What Ruff did automatically:**
- Added two blank lines after imports and between top-level functions.
- Added spaces around operators (`total = 0`, `+=`, `*`).
- Converted single quotes to double quotes (Python standard).
- Reformatted the long list to one item per line.
- Removed the extra spaces in `def   calculate_total`.

You write the logic. Ruff handles the style.

---

## Common lint warnings

Ruff also catches code problems — not just style. These appear as underlines in VS Code:

**Unused imports:**

```python
import os
import sys   # ⚠️ F401: 'sys' imported but unused

print("hello")
```

**Unused variables:**

```python
def calculate(base, tax):
    discount = 10  # ⚠️ F841: local variable 'discount' is assigned but never used
    return base + tax
```

**Unreachable code:**

```python
def check_age(age):
    return "Adult"
    print("Minor")  # ⚠️ code after return is unreachable
```

**Wrong None comparison:**

```python
if user == None:   # ⚠️ E711: use 'is None' instead of '== None'
    print("no user")
```

**Mutable default argument:**

```python
def add_item(item, items=[]):  # ⚠️ B006: mutable default argument
    items.append(item)
    return items
```

**Outdated syntax:**

```python
from typing import List, Dict   # ⚠️ UP006: use list, dict instead
def process(items: List[str]) -> Dict[str, int]:
    ...
```

---

## Configuration

Add Ruff configuration to `pyproject.toml` (the same file used for packaging and other tools):

```toml
[tool.ruff]
# Maximum line length — 88 is the Ruff/Black default
line-length = 88

# Python target version
target-version = "py310"

# Files and directories to exclude
exclude = [
    ".git",
    ".venv",
    "__pycache__",
    "*.egg-info",
]

[tool.ruff.lint]
# Rule sets to enable
select = [
    "E",   # pycodestyle errors
    "F",   # pyflakes (undefined names, unused imports)
    "I",   # isort (import ordering)
    "B",   # flake8-bugbear (likely bugs)
    "UP",  # pyupgrade (modernise syntax)
    "N",   # pep8-naming conventions
]

# Rules to ignore
ignore = [
    "E501",  # line too long — handled by formatter
]

# Fix automatically when possible
fixable = ["ALL"]

[tool.ruff.format]
# Use double quotes (default)
quote-style = "double"

# Use spaces (not tabs)
indent-style = "space"
```

### Minimal starter config

If you are just starting out, this is enough:

```toml
[tool.ruff.lint]
select = ["E", "F", "I"]
```

Ruff works with zero configuration too — sensible defaults out of the box.

---

## Rule sets

Ruff has hundreds of rules organised into sets. These are the most useful ones:

| Code | Name | What it catches |
|---|---|---|
| `E` | pycodestyle | Spacing, blank lines, indentation |
| `F` | pyflakes | Undefined names, unused imports/variables |
| `I` | isort | Import order and grouping |
| `B` | flake8-bugbear | Likely bugs (mutable defaults, bare `except`, etc.) |
| `UP` | pyupgrade | Outdated syntax (`List[int]` → `list[int]`, etc.) |
| `N` | pep8-naming | Naming conventions (snake_case, PascalCase, etc.) |
| `S` | bandit | Security issues (hardcoded passwords, `eval`, etc.) |
| `C4` | flake8-comprehensions | Suggest better comprehensions |
| `SIM` | flake8-simplify | Suggest simpler code patterns |

### Exploring rules

```bash
ruff rule F401       # explain a specific rule
ruff rule --all      # list all available rules
```

### Recommended config for AI engineering projects

```toml
[tool.ruff.lint]
select = [
    "E", "F", "I",   # essential
    "B",             # catch likely bugs
    "UP",            # keep syntax modern
    "S",             # security
    "SIM",           # simplifications
]
ignore = [
    "S101",   # allow assert in tests
    "S603",   # subprocess — needed in some tools
]
```

---

## CLI usage

```bash
# Check for lint errors
ruff check .                    # entire project
ruff check my_file.py           # single file

# Format code
ruff format .                   # entire project
ruff format my_file.py          # single file
ruff format --check .           # preview what would change

# Fix lint errors automatically
ruff check --fix .              # auto-fix what can be fixed
ruff check --fix --diff .       # preview fixes without applying

# Both lint+fix and format in one command
ruff check --fix . && ruff format .
```

### Integrate into your workflow

Add a `Makefile` or shell script at the project root:

```makefile
# Makefile
lint:
	ruff check .

format:
	ruff format .

fix:
	ruff check --fix . && ruff format .
```

```bash
make fix   # lint, fix and format in one command
```

---

## Suppressing rules with # noqa

Sometimes you need to suppress a rule for a specific line. Use `# noqa`:

```python
import sys  # noqa: F401   — needed to register plugin, not used directly

# For multiple rules
import os, sys  # noqa: E401, F401

# Suppress all rules on one line (use sparingly)
result = very_long_function_call(a, b, c, d, e, f)  # noqa
```

### When to use # noqa

✅ Valid cases:
- Imports that look unused but trigger side effects (Django signal registration, plugin loading).
- Unavoidably long URLs or generated strings.
- Standard mathematical naming (e.g. matrix `A`, `B`).
- Auto-generated files you do not control.

❌ Never use # noqa to:
- Hide real bugs.
- Avoid learning to write clean code.
- Silence errors you do not understand.

### Suppress entire files

In `pyproject.toml`:

```toml
[tool.ruff.lint]
exclude = [
    "src/generated/*.py",
    "legacy/",
]
```

### Rule codes in error messages

When Ruff reports an error, the code is in the message:

```
my_file.py:5:8: F401 [*] `sys` imported but unused
                    ^^^^
                    This is the code to use in # noqa: F401
```

---

## pre-commit integration

`pre-commit` runs checks automatically before every `git commit`, preventing broken or unformatted code from entering the repository.

### Setup

```bash
# Install pre-commit
uv add --dev pre-commit
```

Create `.pre-commit-config.yaml` at the project root:

```yaml
repos:
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.4.4   # use the latest version
    hooks:
      - id: ruff           # lint and fix
        args: [--fix]
      - id: ruff-format    # format
```

```bash
# Install the git hooks
pre-commit install

# Run manually on all files
pre-commit run --all-files
```

From now on, every `git commit` automatically runs Ruff. If there are unfixed issues, the commit is blocked and you see exactly what needs fixing.

### Typical project setup

```
my_project/
├── pyproject.toml          ← ruff config here
├── .pre-commit-config.yaml ← pre-commit hooks
├── src/
│   └── my_package/
└── tests/
```

```toml
# pyproject.toml — complete example
[tool.ruff]
line-length = 88
target-version = "py310"

[tool.ruff.lint]
select = ["E", "F", "I", "B", "UP"]
ignore = ["E501"]
fixable = ["ALL"]

[tool.ruff.format]
quote-style = "double"
indent-style = "space"
```

---

## Summary

- **Ruff** replaces Black, isort, Flake8, Pylint and more — one tool, one config.
- **Install** via the VS Code extension (Astral) and `uv add --dev ruff`.
- **Format on save** — enable in VS Code settings for zero-friction style.
- **Key rule sets**: `E` + `F` + `I` as minimum; add `B`, `UP`, `S` for professional projects.
- **Configure** in `pyproject.toml` under `[tool.ruff]` and `[tool.ruff.lint]`.
- **CLI**: `ruff check .` to lint, `ruff format .` to format, `ruff check --fix .` to auto-fix.
- **`# noqa: CODE`** to suppress specific rules on a line — use sparingly.
- **pre-commit** to enforce Ruff on every commit — the professional standard.

In the next lesson we will cover dependency management with `uv` — the modern, fast replacement for pip and virtualenv.