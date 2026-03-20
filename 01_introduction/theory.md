# 01 — Introduction to Python

Python is one of the most popular programming languages in the world — and for good reason. It is simple enough for beginners, powerful enough for production systems, and dominates the AI and data science ecosystem. This lesson covers what Python is, how to run it, and the conventions you need to know from day one.

---

## What is Python?

Python is a high-level, interpreted, general-purpose programming language created by [Guido van Rossum](https://en.wikipedia.org/wiki/Guido_van_Rossum) and first released in 1991. It is known for its clean, readable syntax, which makes it easy to learn and fast to develop with.

### What is Python used for?

Python is one of the most versatile languages available and is used across many domains:

- **Web development** — building web applications and APIs (Django, Flask, FastAPI)
- **Data science and analysis** — processing, analysing and visualising data (pandas, NumPy, matplotlib)
- **Artificial intelligence and machine learning** — training models and building AI systems (PyTorch, TensorFlow, scikit-learn)
- **Automation and scripting** — automating repetitive tasks and processes
- **Cybersecurity** — vulnerability analysis and penetration testing
- **Finance** — quantitative analysis and algorithmic trading

### Key characteristics

**1. Clear and readable syntax**
Python uses a simple, minimalist syntax based on indentation. Code reads almost like plain English.

**2. Interpreted**
Python executes code line by line without needing to compile first. This makes experimentation fast and feedback immediate.

**3. Multi-paradigm**
Python supports structured, object-oriented and functional programming. You can choose the style that best fits the problem.

**4. Extensive ecosystem**
Python has thousands of libraries covering almost every domain — from web development to AI to finance.

**5. Active community**
Python has one of the largest developer communities in the world, with abundant resources, tutorials and support.

**6. Portable**
Python runs on Windows, macOS and Linux without modifying your code.

---

## Your first Python program

The first program in any language is traditionally "Hello, World!". In Python, it looks like this:

```python
print("Hello, World!")
```

`print()` is a built-in Python function that displays text in the console. It is one of the most basic and frequently used functions in the language.

### More examples with print()

```python
# Print multiple elements
print("Hello", "Python")  # Output: Hello Python

# Change the separator
print("Hello", "Python", sep="-")  # Output: Hello-Python

# Print numbers
print(42)  # Output: 42

# Combine text and numbers
print("The answer is", 42)  # Output: The answer is 42
```

---

## Comments

Comments are lines that Python ignores when executing code. They exist for humans — to explain what the code does and why.

### Single-line comments

```python
# This is a single-line comment
print("Hello")  # You can also comment at the end of a line
```

### Multi-line comments

```python
"""
This is a multi-line comment.
Python ignores it during execution.
"""
```

> **Note**: Triple quotes are technically **docstrings** when placed at the start of functions, classes or modules. When used elsewhere, Python treats them as strings that are not assigned to anything — effectively comments.

### Good practices

- Comments should explain **why**, not **what**.
- Avoid obvious comments like `x = 5  # Assign 5 to x`.
- Use comments to explain design decisions or complex logic.
- Keep comments up to date with the code.

```python
# We use a dictionary instead of a list for O(1) lookups
cache = {}
```

---

## How to run Python code

There are three main ways to run Python code. Each has its place depending on what you are trying to do.

### 1. REPL (Read-Eval-Print Loop)

The interactive Python interpreter. Ideal for quick experiments and testing small snippets.

```bash
python3
>>> print("Hello")
Hello
>>> 2 + 2
4
```

To exit: `exit()` or `Ctrl+D` (macOS/Linux) / `Ctrl+Z` (Windows).

### 2. .py files

Save your code in a file with a `.py` extension and run it from the terminal. This is how real software is built.

```python
# file: hello.py
print("Hello from a file")
```

```bash
python3 hello.py
```

### 3. Jupyter Notebooks (.ipynb)

An interactive environment that combines code, text and visualisations in a single document. Very popular in data science and research.

---

## .py vs .ipynb — which one should you use?

Both formats run Python, but they serve different purposes. Understanding the difference from the start will save you confusion later.

### .py files

A `.py` file is a plain Python script. It runs from top to bottom, is easy to version with Git, and is the standard format for software development.

```python
# hello.py

def greet(name: str) -> str:
    return f"Hello, {name}!"

print(greet("World"))
```

Run it from the terminal:

```bash
python3 hello.py
# Output: Hello, World!
```

**Use .py when:**
- Building applications, APIs or tools.
- Writing reusable modules or packages.
- Working in a production environment.
- Collaborating on a software project.

### Jupyter Notebooks (.ipynb)

A notebook is made up of cells — each cell can contain either code or text (Markdown). You run cells individually and see the output immediately below each one.

```
# Cell 1 (Markdown)
## Exploring the data

# Cell 2 (Code)
import pandas as pd
df = pd.read_csv("data.csv")
df.head()

# Cell 3 (Code)
df.describe()
```

**Use notebooks when:**
- Exploring data interactively.
- Building reports that combine code, charts and explanation.
- Learning or teaching step by step.
- Working in data science or research contexts.

### Summary

| | .py | .ipynb |
|---|---|---|
| Format | Plain script | Interactive cells |
| Execution | Top to bottom | Cell by cell |
| Git-friendly | ✅ Clean diffs | ⚠️ Noisy diffs |
| Best for | Development, production | Exploration, data science |
| Standard in | Software engineering | Data science, ML research |

**In this repository we use `.py` files.** This keeps things close to how professional software is built. You will encounter notebooks in other repositories in this ecosystem — particularly in `data-fundamentals` and `llm-fundamentals`.

---

## Setting up VS Code

Visual Studio Code (VS Code) is the editor we recommend for this repository. It is free, extensible and has excellent Python support.

### Installation

1. Go to [code.visualstudio.com](https://code.visualstudio.com/) and download the installer for your OS.
2. Follow the installation steps:
   - **Windows**: make sure to check **"Add to PATH"** during installation.
   - **macOS**: drag VS Code to your Applications folder.

Alternatively, on macOS with Homebrew:

```bash
brew install --cask visual-studio-code
```

### Essential extensions

**Python** (by Microsoft)
Adds IntelliSense, linting, debugging and more. This is the core extension for Python development in VS Code.

**Pylance** (by Microsoft)
Provides better autocompletion and type checking. It is usually installed automatically alongside the Python extension — worth verifying.

### One important setting

After installing the Python extension, change this setting:

1. Open Settings (`Cmd+,` on macOS / `Ctrl+,` on Windows).
2. Search for `Python terminal execute in file directory`.
3. **Enable it.**

This makes VS Code run your Python files from the file's own directory instead of the workspace root. It avoids a lot of confusing path errors when you start working with files.

### Running a Python file in VS Code

Once everything is set up, you can run a `.py` file in three ways:

- Click the **▶️ play button** in the top right corner.
- Right-click the file → **Run Python File in Terminal**.
- Open the terminal (`Ctrl/Cmd+J`) and run `python3 filename.py` manually.

---

## Code style — PEP 8

Python has an official style guide called **PEP 8**. Following it makes your code consistent and readable by any Python developer.

### Naming conventions

```python
# Variables and functions — snake_case
my_variable = 10
full_name = "Javi"

def calculate_average():
    pass

# Classes — PascalCase
class MyClass:
    pass

class ActiveUser:
    pass

# Constants — UPPER_CASE
PI = 3.14159
MAX_RETRIES = 3
```

### Indentation

Always use **4 spaces** — never tabs. Indentation is not optional in Python; it defines code blocks.

```python
if True:
    print("This is indented with 4 spaces")
```

### Spacing

- Two blank lines between top-level functions and classes.
- One blank line between methods inside a class.
- Spaces around operators: `x = 1 + 2`, not `x=1+2`.

We will cover code formatting in depth in lesson `13_code_formatting_ruff`, where we use **Ruff** to enforce these rules automatically.

---

## The Zen of Python

The Zen of Python is a set of principles that guide the philosophy of the language. Written by Tim Peters, it captures the values that make Python code good. Run this in your terminal to see it:

```python
import this
```

A few principles worth internalising from day one:

**"Beautiful is better than ugly."**
Write code you are proud to read.

**"Explicit is better than implicit."**
Do not hide what your code is doing. Make intent clear.

**"Simple is better than complex."**
If you can solve it simply, do not over-engineer it.

**"Readability counts."**
Code is read far more often than it is written. Optimise for the reader.

**"There should be one — and preferably only one — obvious way to do it."**
Python promotes a clear, preferred way to solve each problem. This makes code consistent across different developers.

These are not abstract ideals — they will influence every decision you make as you write Python throughout this roadmap.

---

## Summary

- Python is a high-level, interpreted, multi-paradigm language used across web, data, AI and automation.
- `print()` is your first tool — use it to display output and debug.
- Comments explain **why**, not what. Keep them honest and up to date.
- Use `.py` files for development and production. Use notebooks for exploration and data science.
- VS Code with the Python and Pylance extensions is the recommended setup.
- Follow PEP 8 from the start — consistency matters.
- The Zen of Python is not decoration. It is how good Python code thinks.

In the next lesson we will cover variables, data types and how Python stores information.