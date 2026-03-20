# 11 — File Handling

Working with files is a fundamental programming task. Whether you are reading configuration, processing data, writing logs or saving results, you need to interact with the file system. Python provides intuitive, safe tools for all of these.

---

## Why file handling matters

Files enable:
- **Data persistence** — information that survives program termination.
- **Data exchange** — sharing data between programs and systems.
- **Large data processing** — working with data that does not fit in memory.
- **Configuration** — storing settings and preferences.
- **Logging** — recording events and errors.

---

## open() — modes and encoding

`open()` is the entry point for file operations. It returns a file object:

```python
open(filename, mode="r", encoding="utf-8")
```

Always specify `encoding="utf-8"` for text files — behaviour varies by platform if you omit it.

### Modes

| Mode | Description | File missing | File exists |
|---|---|---|---|
| `"r"` | Read (default) | Error | Reads from start |
| `"w"` | Write | Creates new | Overwrites |
| `"a"` | Append | Creates new | Adds to end |
| `"x"` | Exclusive create | Creates new | Error |
| `"r+"` | Read and write | Error | Reads/writes |
| `"b"` | Binary modifier (`"rb"`, `"wb"`) | — | — |

### Always use with

The `with` statement (context manager) guarantees the file is closed, even if an exception occurs. We covered context managers in lessons `07` and `09` — here we simply apply them:

```python
# ❌ Risky — file stays open if an error occurs
f = open("data.txt", "r", encoding="utf-8")
content = f.read()
f.close()

# ✅ Always use with
with open("data.txt", "r", encoding="utf-8") as f:
    content = f.read()
# file is automatically closed here
```

---

## Reading files

### read() — entire file as a string

```python
with open("document.txt", "r", encoding="utf-8") as f:
    content = f.read()
    print(f"Characters: {len(content)}")
```

Use when the file is small enough to fit in memory and you need all of it at once.

### read(n) — read n characters

```python
with open("document.txt", "r", encoding="utf-8") as f:
    first_100 = f.read(100)
    next_50 = f.read(50)   # continues from where it left off
```

### readline() — one line at a time

```python
with open("document.txt", "r", encoding="utf-8") as f:
    line1 = f.readline()   # includes the trailing \n
    line2 = f.readline().strip()  # strip() removes \n
```

### readlines() — all lines as a list

```python
with open("document.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()  # [" line1\n", "line2\n", ...]
    print(f"Lines: {len(lines)}")
```

Loads the entire file into memory — avoid for large files.

### Iterate over the file (recommended for large files)

The most memory-efficient way to process files line by line:

```python
with open("document.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())
```

Python reads one line at a time — the entire file is never in memory at once. This is the approach to use for log files, large datasets and streaming pipelines.

---

## Writing files

### write() — write a string

Does **not** add a newline automatically:

```python
with open("output.txt", "w", encoding="utf-8") as f:
    f.write("First line\n")
    f.write("Second line\n")
```

Mode `"w"` creates the file if it does not exist and **overwrites** it if it does.

### writelines() — write a list of strings

Also does **not** add newlines between elements:

```python
lines = ["First line", "Second line", "Third line"]

# ❌ No newlines — everything on one line
with open("output.txt", "w", encoding="utf-8") as f:
    f.writelines(lines)

# ✅ Add newlines explicitly
with open("output.txt", "w", encoding="utf-8") as f:
    f.writelines(line + "\n" for line in lines)
```

### Append mode

Adds to the end of the file without erasing existing content:

```python
with open("app.log", "a", encoding="utf-8") as f:
    f.write("2026-01-15 09:30:00 INFO Server started\n")

# Later in the program:
with open("app.log", "a", encoding="utf-8") as f:
    f.write("2026-01-15 09:31:05 INFO Request received\n")
```

### Exclusive create — x mode

Fails if the file already exists — useful to prevent accidental overwrites:

```python
try:
    with open("config.json", "x", encoding="utf-8") as f:
        f.write('{"version": "1.0"}')
except FileExistsError:
    print("Config file already exists — skipping creation")
```

---

## pathlib as the primary interface

`pathlib.Path` is the modern, recommended way to work with file paths in Python. We introduced it in lesson `10_modular_programming` — here we use it fully.

```python
from pathlib import Path

# Create a Path object
p = Path("data/results.txt")

# Inspect
print(p.name)      # "results.txt"
print(p.stem)      # "results"
print(p.suffix)    # ".txt"
print(p.parent)    # Path("data")

# Check state
p.exists()         # True/False
p.is_file()        # True/False
p.is_dir()         # True/False

# Build paths safely (cross-platform)
base = Path("data")
output = base / "2026" / "january" / "report.txt"

# Create directories
Path("output/logs").mkdir(parents=True, exist_ok=True)

# Read and write directly
content = p.read_text(encoding="utf-8")
p.write_text("new content", encoding="utf-8")

# File metadata
size = p.stat().st_size   # bytes
```

### Listing files

```python
from pathlib import Path

# All files in a directory
for f in Path("data").iterdir():
    print(f.name)

# Files matching a pattern
python_files = list(Path(".").glob("*.py"))
all_logs = list(Path("logs").glob("**/*.log"))  # recursive

# Get all CSV files and sort by name
csv_files = sorted(Path("data").glob("*.csv"))
```

### pathlib vs os.path

`pathlib` is the modern standard. `os.path` is the older API you will encounter in legacy code:

```python
# os.path (legacy — still works)
import os
os.path.join("data", "file.txt")
os.path.exists("data/file.txt")
os.makedirs("data/output", exist_ok=True)

# pathlib (modern — prefer this)
from pathlib import Path
Path("data") / "file.txt"
Path("data/file.txt").exists()
Path("data/output").mkdir(parents=True, exist_ok=True)
```

---

## Working with CSV files

CSV (comma-separated values) is the most common structured text format in data and AI engineering. Python's `csv` module handles edge cases correctly — quoting, special characters, different delimiters.

### Reading CSV

```python
import csv
from pathlib import Path

with open("users.csv", "r", encoding="utf-8", newline="") as f:
    reader = csv.reader(f)
    header = next(reader)   # first row is the header
    print(f"Columns: {header}")

    for row in reader:
        print(row)  # list of strings
```

> Always pass `newline=""` when opening CSV files — the `csv` module handles line endings itself.

### Reading CSV as dicts

`DictReader` maps each row to a dict using the header row as keys:

```python
import csv

with open("users.csv", "r", encoding="utf-8", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row["name"], row["age"])
```

### Writing CSV

```python
import csv

rows = [
    ["name", "age", "city"],
    ["Ana", "28", "Madrid"],
    ["Juan", "35", "Barcelona"],
]

with open("output.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(rows)
```

### Writing CSV from dicts

```python
import csv

users = [
    {"name": "Ana", "age": 28, "city": "Madrid"},
    {"name": "Juan", "age": 35, "city": "Barcelona"},
]

with open("output.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "age", "city"])
    writer.writeheader()
    writer.writerows(users)
```

### Custom delimiters

```python
# TSV (tab-separated values)
with open("data.tsv", "r", encoding="utf-8", newline="") as f:
    reader = csv.reader(f, delimiter="\t")
    for row in reader:
        print(row)

# Semicolon-separated (common in European locales)
with open("data.csv", "r", encoding="utf-8", newline="") as f:
    reader = csv.reader(f, delimiter=";")
```

---

## Binary files

Use binary mode (`"b"`) for non-text files: images, audio, PDFs, compiled files.

```python
# Read binary file
with open("image.jpg", "rb") as f:
    data = f.read()
    print(f"Size: {len(data)} bytes")

# Write binary file
with open("copy.jpg", "wb") as f:
    f.write(data)

# Copy binary file efficiently (chunk by chunk — no memory issues)
def copy_file(source: str, destination: str, chunk_size: int = 8192):
    with open(source, "rb") as src, open(destination, "wb") as dst:
        while chunk := src.read(chunk_size):
            dst.write(chunk)

copy_file("large_model.bin", "backup/large_model.bin")
```

---

## Error handling

```python
from pathlib import Path

def read_config(path: str) -> str:
    try:
        return Path(path).read_text(encoding="utf-8")
    except FileNotFoundError:
        print(f"Config not found: {path}")
        return ""
    except PermissionError:
        print(f"No permission to read: {path}")
        return ""
    except IsADirectoryError:
        print(f"{path} is a directory, not a file")
        return ""
    except UnicodeDecodeError:
        print(f"Cannot decode {path} as UTF-8 — try binary mode")
        return ""
```

### Safe write with atomic replace

Writing directly can corrupt a file if the process is interrupted. Write to a temp file first, then rename:

```python
import os
from pathlib import Path

def safe_write(path: str, content: str):
    """Write atomically — avoids corrupting existing file on failure."""
    tmp = path + ".tmp"
    try:
        Path(tmp).write_text(content, encoding="utf-8")
        os.replace(tmp, path)   # atomic on POSIX systems
    except Exception:
        Path(tmp).unlink(missing_ok=True)
        raise
```

---

## tempfile — temporary files

The `tempfile` module creates temporary files and directories that are automatically deleted. Essential in testing and AI pipelines where you need scratch space:

```python
import tempfile
from pathlib import Path

# Temporary file — deleted when closed
with tempfile.NamedTemporaryFile(mode="w", suffix=".txt",
                                  encoding="utf-8", delete=True) as f:
    f.write("temporary content")
    print(f"Temp file: {f.name}")
# file is deleted here

# Temporary directory — deleted with all contents on exit
with tempfile.TemporaryDirectory() as tmp_dir:
    tmp_path = Path(tmp_dir)
    output_file = tmp_path / "result.txt"
    output_file.write_text("result data", encoding="utf-8")
    print(f"Temp dir: {tmp_dir}")
    # process output_file...
# directory and all contents are deleted here
```

**Practical use in AI engineering:**

```python
import tempfile
import json

def process_model_output(data: dict, processor) -> dict:
    """Process model output via a temporary file."""
    with tempfile.NamedTemporaryFile(
        mode="w", suffix=".json", encoding="utf-8", delete=False
    ) as f:
        json.dump(data, f)
        tmp_path = f.name

    try:
        result = processor(tmp_path)
    finally:
        Path(tmp_path).unlink(missing_ok=True)

    return result
```

---

## Best practices

**Always use `with`** — never manage file closing manually.

**Always specify encoding** — use `encoding="utf-8"` for all text files.

**Use `pathlib.Path`** — it is cross-platform, readable and more powerful than string concatenation.

**Iterate for large files** — never `read()` or `readlines()` a file that might be gigabytes:

```python
# ❌ Loads entire file into memory
lines = open("huge.log").readlines()

# ✅ Processes one line at a time
with open("huge.log", encoding="utf-8") as f:
    for line in f:
        process(line)
```

**Use `csv` module for CSV files** — never `split(",")` manually (breaks on quoted fields with commas):

```python
# ❌ Breaks on: "Smith, John",30,"New York, NY"
row = line.split(",")

# ✅ Handles all edge cases correctly
reader = csv.reader(f)
```

**Handle exceptions explicitly** — catch `FileNotFoundError`, `PermissionError` and `UnicodeDecodeError` separately.

**Use `tempfile` for scratch files** — never create temp files manually in `/tmp` or the current directory.

**Prefer absolute paths** for files outside the project — use `pathlib.Path.resolve()` to convert relative to absolute.

---

## Summary

- **`open(mode, encoding)`** — always specify encoding for text files. Always use `with`.
- **Reading**: `read()` for small files, iterate with `for line in f` for large ones.
- **Writing**: `"w"` overwrites, `"a"` appends, `"x"` fails if exists.
- **`pathlib.Path`** — the modern cross-platform interface for all path operations.
- **CSV** — use the `csv` module (`reader`, `writer`, `DictReader`, `DictWriter`). Always pass `newline=""` to `open()`.
- **Binary mode** — use `"rb"` / `"wb"` for non-text files. Read in chunks for large files.
- **Error handling** — catch `FileNotFoundError`, `PermissionError`, `UnicodeDecodeError`.
- **`tempfile`** — for temporary scratch files in tests and pipelines.

In the next lesson we will cover type hints — how to annotate your code for better tooling and readability.