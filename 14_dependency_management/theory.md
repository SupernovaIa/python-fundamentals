# 14 — Dependency Management

Every real Python project depends on external packages. Managing those dependencies — which packages, which versions, in isolated environments — is one of the most important practical skills in Python engineering. This lesson covers the modern way to do it with `uv`.

---

## Why dependency management matters

Imagine this situation:

- **Project A** needs `requests` version 1.0
- **Project B** needs `requests` version 2.0

If you install 2.0 globally for Project B, Project A breaks. Without isolation, every project fights over the same global Python installation.

**The solution**: virtual environments — isolated copies of Python with their own packages, one per project.

```
project_a/
  .venv/          ← isolated environment
    requests 1.0

project_b/
  .venv/          ← different isolated environment
    requests 2.0
```

Each project lives in its own bubble. What you install for one does not affect the other.

---

## The old way — venv and pip

Before `uv`, the standard approach was:

```bash
# Create a virtual environment
python -m venv .venv

# Activate it (must do this in every new terminal)
source .venv/bin/activate    # macOS/Linux
.venv\Scripts\activate       # Windows

# Install packages
pip install requests pandas

# Save dependencies to a file
pip freeze > requirements.txt

# Someone else installs from it
pip install -r requirements.txt
```

This works but has problems:
- Activation is manual and easy to forget.
- `pip freeze` captures everything including transitive dependencies, making `requirements.txt` noisy.
- No built-in lockfile — exact reproducibility is hard.
- pip is slow compared to modern alternatives.

You will encounter this workflow in legacy projects. Knowing it helps you understand what `uv` does under the hood — and why it is better.

---

## uv — the modern standard

`uv` is a Python package and project manager written in Rust. It is 10–100× faster than pip and replaces the entire `pip` + `venv` + `pip-tools` toolchain with a single command.

`uv` handles:
- Creating and managing virtual environments automatically.
- Installing and removing packages.
- Generating lockfiles for exact reproducibility.
- Running scripts in the right environment.
- Managing Python versions.

### Installing uv

```bash
# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

# Or with pip (if you already have Python)
pip install uv
```

```bash
# Verify installation
uv --version
```

---

## uv workflow

### Initialise a new project

```bash
uv init my_project
cd my_project
```

This creates:

```
my_project/
├── .python-version    ← Python version for this project
├── pyproject.toml     ← project metadata and dependencies
├── README.md
└── hello.py
```

For an existing project, just run `uv init` in the project directory.

### Add dependencies

```bash
# Add a package
uv add requests

# Add multiple packages
uv add fastapi langchain openai

# Add a specific version
uv add "requests>=2.28,<3"

# Add a dev-only dependency (not included in production)
uv add --dev ruff pytest pre-commit
```

`uv add` automatically:
1. Creates `.venv/` if it does not exist.
2. Installs the package.
3. Updates `pyproject.toml`.
4. Updates `uv.lock`.

### Remove dependencies

```bash
uv remove requests
uv remove --dev ruff
```

### Update dependencies

```bash
# Update a specific package to its latest compatible version
uv add --upgrade requests

# Update all packages
uv lock --upgrade

# Inspect a specific package
uv pip show requests    # version, location, dependencies
uv pip list             # all installed packages
```

### Sync — install everything from pyproject.toml

```bash
# Install all dependencies declared in pyproject.toml
uv sync

# Install including dev dependencies
uv sync --dev
```

Use `uv sync` when you clone a project or pull changes — it brings your environment up to date.

### Run commands in the project environment

```bash
# Run a Python file
uv run python main.py

# Run a tool
uv run ruff check .
uv run pytest

# Run Python interactively
uv run python
```

`uv run` activates the virtual environment automatically — no manual activation needed.

### Install tools globally

```bash
# Install CLI tools globally (not tied to a project)
uv tool install ruff
uv tool install httpie
uv tool install pre-commit

# Run a tool without installing permanently
uvx ruff check .
```

### Manage Python versions

```bash
# Install a specific Python version
uv python install 3.12

# Use a specific version for your project
uv python pin 3.11

# List available Python versions
uv python list
```

---

## pyproject.toml for dependencies

`pyproject.toml` is the single source of truth for your project — it replaces `setup.py`, `setup.cfg` and `requirements.txt`. We introduced it in lesson `10_modular_programming` for packaging. Here we focus on the dependency section.

```toml
[project]
name = "my-project"
version = "0.1.0"
description = "My Python project"
requires-python = ">=3.10"

# Runtime dependencies — needed in production
dependencies = [
    "requests>=2.28",
    "fastapi>=0.100",
    "openai>=1.0",
]

[project.optional-dependencies]
# Dev dependencies — only needed during development
dev = [
    "ruff>=0.4",
    "pytest>=8.0",
    "pre-commit>=3.0",
]

[build-system]
requires = ["setuptools>=61"]
build-backend = "setuptools.build_meta"
```

When using `uv`, the dev dependencies live in a dedicated section:

```toml
[tool.uv]
dev-dependencies = [
    "ruff>=0.4",
    "pytest>=8.0",
    "pre-commit>=3.0",
]
```

`uv add` and `uv add --dev` maintain these sections automatically — you rarely need to edit `pyproject.toml` by hand.

---

## uv.lock — exact reproducibility

Every time you `uv add` a package, `uv` generates a `uv.lock` file. This is a **lockfile** — it records the exact version of every package (including transitive dependencies) that was installed.

```
# uv.lock (excerpt — managed automatically, do not edit by hand)
version = 1
requires-python = ">=3.10"

[[package]]
name = "requests"
version = "2.31.0"
source = { registry = "https://pypi.org/simple" }
dependencies = [
  { name = "certifi" },
  { name = "charset-normalizer" },
  { name = "idna" },
  { name = "urllib3" },
]

[[package]]
name = "certifi"
version = "2024.2.2"
...
```

**Why the lockfile matters:**

- `pyproject.toml` says `"requests>=2.28"` — a range.
- `uv.lock` says `"requests==2.31.0"` — the exact version.
- When your colleague runs `uv sync`, they get **exactly the same versions** you have.
- CI/CD pipelines reproduce your environment exactly.

**Commit `uv.lock` to Git.** It is the contract that makes your project reproducible across machines and over time.

```bash
# Always commit both
git add pyproject.toml uv.lock
git commit -m "add requests dependency"
```

---

## .gitignore — what not to commit

Never commit the virtual environment itself — it is large (hundreds of MB), platform-specific and always reproducible from `pyproject.toml` + `uv.lock`.

Create a `.gitignore` file at the project root:

```gitignore
# Virtual environment
.venv/
venv/
env/

# Python cache
__pycache__/
*.py[cod]
*.pyo
*.pyd
.Python

# Distribution and packaging
dist/
build/
*.egg-info/
*.egg

# Type checker
.mypy_cache/
.pyright/
.ruff_cache/

# Testing
.pytest_cache/
.coverage
htmlcov/

# Environment variables (never commit secrets)
.env
.env.local
.env.*.local

# OS files
.DS_Store
Thumbs.db

# IDE
.vscode/settings.json
.idea/
```

GitHub provides a Python `.gitignore` template — use it as a starting point.

### What to always commit

```
✅ pyproject.toml     — dependency declarations
✅ uv.lock            — exact versions (reproducibility)
✅ .python-version    — Python version for the project
✅ .gitignore         — exclusion rules
✅ README.md          — project documentation
✅ src/               — your actual code
```

---

## requirements.txt — legacy compatibility

`requirements.txt` is the old format you will encounter in many existing projects. You do not need it in new projects that use `uv`, but you need to know how to work with it.

### Reading a requirements.txt project

```bash
# If a project only has requirements.txt, install with uv:
uv pip install -r requirements.txt

# Or migrate to pyproject.toml:
uv init --name my-project .
uv add -r requirements.txt   # adds all packages to pyproject.toml
```

### Migrating from a venv + pip project

```bash
cd existing-project

# Activate the old venv to get the package list
source .venv/bin/activate
pip freeze > old-requirements.txt
deactivate

# Initialise uv and migrate
uv init --name my-project .
uv add -r old-requirements.txt
rm old-requirements.txt
```

### Generating requirements.txt from uv

If you need to produce a `requirements.txt` for compatibility with a tool that requires it:

```bash
uv pip compile pyproject.toml -o requirements.txt
```

### The requirements.txt format

```text
# Pinned versions (from pip freeze)
requests==2.31.0
certifi==2024.2.2
charset-normalizer==3.3.2

# Ranges (human-written)
requests>=2.28,<3
fastapi>=0.100

# Install from a local path
-e ./my_local_package

# Install from git
git+https://github.com/user/repo.git@main
```

---

## Common errors and solutions

### ModuleNotFoundError — package not found

```python
import requests
# ModuleNotFoundError: No module named 'requests'
```

**Causes:**
1. Package not installed — run `uv add requests`.
2. Wrong environment active — check that VS Code uses `.venv` as interpreter.
3. Running `python` directly instead of `uv run python`.

**Fix:** Always use `uv run python` or ensure VS Code selects `.venv/`.

### Wrong interpreter in VS Code

If VS Code shows the wrong Python path in the status bar (bottom right):
1. Click the Python version in the status bar.
2. Select the interpreter at `.venv/bin/python` (macOS/Linux) or `.venv\Scripts\python.exe` (Windows).

### Dependency conflict

```
error: package 'library-a' requires 'requests<2', but 'library-b' requires 'requests>=2.28'
```

`uv` reports conflicts clearly. Solutions:
- Check if a newer version of one library resolves the conflict.
- Use a compatibility layer or find an alternative package.
- Pin the conflicting package to a version that satisfies both.

```bash
# Try upgrading all packages — often resolves conflicts
uv lock --upgrade
uv sync
```

### Corrupted virtual environment

If the `.venv` becomes corrupted or behaves unexpectedly, delete it and recreate:

```bash
rm -rf .venv        # macOS/Linux
rmdir /s .venv      # Windows

uv sync             # recreates .venv from uv.lock exactly
```

### uv command not found after installation

Restart your terminal. If it persists, add uv to your PATH:

```bash
# macOS/Linux — add to ~/.bashrc or ~/.zshrc
export PATH="$HOME/.local/bin:$PATH"

# Then reload
source ~/.zshrc
```

### Forgot to commit uv.lock

If a colleague gets different package versions, they probably have a stale `uv.lock`. Fix:

```bash
git pull          # get the latest uv.lock
uv sync           # install exactly what uv.lock specifies
```

---

## Full project setup — step by step

Here is the complete workflow for a new project from scratch:

```bash
# 1. Create and enter the project
uv init ai-project
cd ai-project

# 2. Add runtime dependencies
uv add openai langchain fastapi

# 3. Add dev dependencies
uv add --dev ruff pytest pre-commit

# 4. Set up pre-commit (runs ruff on every commit)
pre-commit install

# 5. Verify your environment
uv run python -c "import openai; print('ok')"

# 6. Commit
git init
git add .
git commit -m "initial project setup"
```

When someone else clones your project:

```bash
git clone https://github.com/you/ai-project
cd ai-project
uv sync --dev    # installs everything from uv.lock
uv run python main.py
```

---

## Cheat sheet

```bash
# NEW PROJECT
uv init my-project
cd my-project
uv add requests pandas openai
uv add --dev ruff pytest pre-commit
uv run python main.py

# EXISTING PROJECT (after clone or pull)
git clone repo && cd repo
uv sync --dev
uv run python main.py

# DAILY PACKAGE MANAGEMENT
uv add package              # add runtime dependency
uv add --dev package        # add dev dependency
uv remove package           # remove dependency
uv add --upgrade package    # update one package
uv lock --upgrade           # update all packages
uv pip list                 # list installed packages
uv pip show package         # inspect a package

# RUNNING CODE
uv run python script.py     # run a script
uv run pytest               # run tests
uv run ruff check .         # run a tool

# PYTHON VERSION MANAGEMENT
uv python install 3.12      # install a Python version
uv python pin 3.12          # pin version for this project
uv python list              # list available versions

# GLOBAL TOOLS
uv tool install ruff        # install globally
uvx ruff check .            # run without installing

# LEGACY COMPATIBILITY
uv pip install -r requirements.txt           # install from requirements.txt
uv pip compile pyproject.toml -o req.txt     # generate requirements.txt

# TROUBLESHOOTING
rm -rf .venv && uv sync     # recreate corrupted environment
uv lock --upgrade && uv sync # resolve conflicts with newer versions
```

---



- **Virtual environments** isolate each project's dependencies — one `.venv` per project.
- **The old way**: `python -m venv` + `pip` + `requirements.txt` — still found in legacy projects.
- **The modern way**: `uv` — faster, automatic, reproducible.
- **`uv init`** — initialise a project.
- **`uv add`** / **`uv remove`** — manage dependencies, updates `pyproject.toml` and `uv.lock` automatically.
- **`uv sync`** — install everything declared in `pyproject.toml` from `uv.lock`.
- **`uv run`** — run a command in the project environment without manual activation.
- **`pyproject.toml`** — declares dependencies (ranges). Commit this.
- **`uv.lock`** — records exact versions for reproducibility. Always commit this.
- **`.gitignore`** — never commit `.venv/`, secrets (`.env`) or caches.
- **`requirements.txt`** — legacy format, still common. Use `uv pip install -r` to consume it.

You have now completed the `python-fundamentals` module.