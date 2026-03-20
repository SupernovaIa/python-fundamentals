# 12 — Type Hints

Type hints are annotations that specify what types variables, function parameters and return values are expected to have. They are completely **optional** — Python ignores them at runtime — but they dramatically improve code quality, tooling and maintainability.

---

## Why type hints?

Python is dynamically typed — you do not declare types. This is flexible but can cause problems:

```python
# Without type hints — ambiguous
def process(data):
    return data * 2

process("hello")   # "hellohello"
process(5)         # 10
process([1, 2])    # [1, 2, 1, 2]
# What was intended? There is no way to know.
```

```python
# With type hints — intent is clear
def process(data: str) -> str:
    return data * 2
```

**Benefits:**
- **Self-documenting code** — intent is explicit without reading the body.
- **Early error detection** — static type checkers catch bugs before you run the code.
- **Better IDE support** — precise autocomplete, inline errors, safe refactoring.
- **Easier maintenance** — other developers (and future you) understand the contract immediately.

> Type hints do **not** validate at runtime. Python does not raise errors if you pass the wrong type. You need a static type checker for that — covered at the end of this lesson.

---

## Basic syntax

### Variables

```python
name: str = "Javi"
age: int = 29
height: float = 1.75
active: bool = True
result: None = None

# Annotation without assignment — valid, declares intent
count: int  # no value yet
```

### Functions

```python
def greet(name: str) -> str:
    return f"Hello, {name}!"

def add(a: int, b: int) -> int:
    return a + b

def log(message: str, level: str) -> None:
    # None return type = function returns nothing
    print(f"[{level}] {message}")
```

### Methods in classes

```python
class Calculator:
    def __init__(self, name: str) -> None:
        self.name: str = name
        self.history: list[float] = []

    def add(self, a: float, b: float) -> float:
        result = a + b
        self.history.append(result)
        return result

    def get_history(self) -> list[float]:
        return self.history
```

---

## Built-in collection types

From Python 3.9+ you can use the built-in types directly — no imports needed:

```python
# Lists
numbers: list[int] = [1, 2, 3]
names: list[str] = ["Ana", "Juan"]

# Tuples — fixed length, type per position
point: tuple[float, float] = (10.5, 20.3)
record: tuple[str, int, bool] = ("Javi", 29, True)

# Variable-length tuple of one type
scores: tuple[int, ...] = (85, 92, 78, 95)

# Dicts
ages: dict[str, int] = {"Ana": 25, "Juan": 30}
config: dict[str, bool] = {"debug": True, "verbose": False}

# Sets
tags: set[str] = {"python", "ai", "engineering"}
ids: set[int] = {1, 2, 3}
```

> For Python 3.8 compatibility, import from `typing`:
> ```python
> from typing import List, Tuple, Dict, Set
> numbers: List[int] = [1, 2, 3]
> ```
> This repo requires Python 3.10+, so always use the built-in syntax.

---

## Optional and Union

### X | None — optional values

When a value can be a specific type or `None`, use `X | None`:

```python
# Parameter that may be None
def greet(name: str, title: str | None = None) -> str:
    if title:
        return f"Hello, {title} {name}"
    return f"Hello, {name}"

# Return value that may be None
def find_user(user_id: int) -> str | None:
    if user_id == 1:
        return "Javi"
    return None

result = find_user(1)   # str | None
result = find_user(99)  # None
```

> Pre-3.10 equivalent: `from typing import Optional` → `Optional[str]`

### X | Y — union types

When a value can be one of several types:

```python
def process(value: int | str) -> str:
    if isinstance(value, int):
        return f"Number: {value}"
    return f"Text: {value}"

# Multiple types
def parse(raw: str | int | float) -> float:
    return float(raw)
```

> Pre-3.10 equivalent: `from typing import Union` → `Union[str, int]`

### isinstance() with type hints

Union types pair naturally with `isinstance()` to narrow the type:

```python
def handle(data: str | list[str]) -> list[str]:
    if isinstance(data, str):
        return [data]      # type checker knows: data is str here
    return data            # type checker knows: data is list[str] here
```

---

## Any

`Any` opts out of type checking entirely for a variable:

```python
from typing import Any

def print_anything(value: Any) -> None:
    print(value)

data: Any = "text"
data = 123      # valid
data = [1, 2]   # valid
```

> Use `Any` sparingly — it disables all type checking for that variable. It is a last resort for truly dynamic code or when migrating an untyped codebase gradually.

---

## Callable

For functions passed as arguments:

```python
from typing import Callable

# Callable[[param_types], return_type]
def apply(a: int, b: int, operation: Callable[[int, int], int]) -> int:
    return operation(a, b)

def add(x: int, y: int) -> int:
    return x + y

apply(5, 3, add)       # 8
apply(5, 3, lambda x, y: x * y)  # 15
```

```python
# Callable with no parameters
def run(callback: Callable[[], None]) -> None:
    callback()

# Callable with unknown signature
def log_call(func: Callable[..., Any]) -> None:
    print(f"Calling {func.__name__}")
    func()
```

In AI engineering you will see `Callable` constantly — for hooks, processors, validators and pipeline steps.

---

## Literal

Restricts a value to a specific set of allowed values:

```python
from typing import Literal

def move(direction: Literal["north", "south", "east", "west"]) -> None:
    print(f"Moving {direction}")

move("north")   # ✅
move("up")      # ❌ type checker error

def set_log_level(level: Literal["debug", "info", "warning", "error"]) -> None:
    ...

# Works with numbers and booleans too
def set_verbosity(level: Literal[0, 1, 2]) -> None:
    ...
```

`Literal` is especially useful for model parameters in AI engineering:

```python
from typing import Literal

Provider = Literal["openai", "anthropic", "google", "meta"]
ResponseFormat = Literal["text", "json", "markdown"]

def call_model(
    prompt: str,
    provider: Provider,
    format: ResponseFormat = "text",
) -> str:
    ...
```

---

## TypedDict

Defines a dict with a fixed structure and specific key types — much more precise than `dict[str, Any]`:

```python
from typing import TypedDict

class UserConfig(TypedDict):
    name: str
    age: int
    city: str

def process_user(user: UserConfig) -> str:
    return f"{user['name']} ({user['age']}) from {user['city']}"

user: UserConfig = {"name": "Javi", "age": 29, "city": "Madrid"}
process_user(user)  # ✅
process_user({"name": "Ana"})  # ❌ type checker error — missing keys
```

### Optional keys

```python
from typing import TypedDict, NotRequired  # NotRequired requires Python 3.11+

class ModelConfig(TypedDict):
    name: str
    provider: str
    max_tokens: int
    temperature: NotRequired[float]   # optional
    system_prompt: NotRequired[str]   # optional

# For 3.10 and below, use total=False for all-optional or split into two classes
class ModelConfigRequired(TypedDict):
    name: str
    provider: str

class ModelConfigOptional(ModelConfigRequired, total=False):
    max_tokens: int
    temperature: float
    system_prompt: str
```

`TypedDict` is the right tool for API request/response schemas, config dictionaries and any structured data you would otherwise type as `dict[str, Any]`.

---

## TypeAlias

Creates readable aliases for complex types you use repeatedly:

```python
from typing import TypeAlias

# Simple aliases
Vector: TypeAlias = list[float]
Matrix: TypeAlias = list[list[float]]
JsonDict: TypeAlias = dict[str, Any]

# Domain-specific aliases
Embedding: TypeAlias = list[float]
TokenList: TypeAlias = list[int]
ModelName: TypeAlias = str

def embed(text: str) -> Embedding:
    ...

def tokenise(text: str) -> TokenList:
    ...

# Complex aliases
from typing import TypeAlias, Callable
Processor: TypeAlias = Callable[[str], str]
Pipeline: TypeAlias = list[Processor]

def run_pipeline(text: str, pipeline: Pipeline) -> str:
    for step in pipeline:
        text = step(text)
    return text
```

---

## Protocol

Defines an interface based on behaviour, not inheritance — this is Python's formalisation of duck typing:

```python
from typing import Protocol

class Embedder(Protocol):
    def embed(self, text: str) -> list[float]:
        ...

class OpenAIEmbedder:
    def embed(self, text: str) -> list[float]:
        # call OpenAI API
        return [0.1, 0.2, 0.3]

class LocalEmbedder:
    def embed(self, text: str) -> list[float]:
        # run local model
        return [0.4, 0.5, 0.6]

def build_index(texts: list[str], embedder: Embedder) -> list[list[float]]:
    return [embedder.embed(t) for t in texts]

# Both work — neither inherits from Embedder
build_index(["hello", "world"], OpenAIEmbedder())  # ✅
build_index(["hello", "world"], LocalEmbedder())   # ✅
```

`Protocol` is the correct way to write functions that accept "anything with method X" without forcing a specific inheritance hierarchy. In AI engineering this is essential — you swap model providers, vector stores and retrievers constantly.

```python
class Retriever(Protocol):
    def retrieve(self, query: str, top_k: int) -> list[str]:
        ...

class Reranker(Protocol):
    def rerank(self, query: str, documents: list[str]) -> list[str]:
        ...
```

---

## TypeVar and Generic — brief introduction

`TypeVar` lets you write functions and classes that preserve type information across operations:

```python
from typing import TypeVar

T = TypeVar("T")

def first(items: list[T]) -> T | None:
    return items[0] if items else None

first([1, 2, 3])     # return type inferred as int | None
first(["a", "b"])    # return type inferred as str | None
```

```python
from typing import Generic

class Stack(Generic[T]):
    def __init__(self) -> None:
        self._items: list[T] = []

    def push(self, item: T) -> None:
        self._items.append(item)

    def pop(self) -> T:
        return self._items.pop()

stack: Stack[int] = Stack()
stack.push(1)
stack.push(2)
stack.pop()   # type checker knows this is int
```

We will use `TypeVar` and `Generic` more extensively in later modules — for now, recognise the pattern when you see it.

---

## Checking types — pyright and reveal_type

Type hints are only useful if you actually check them. **Pyright** is the recommended tool — it is what Pylance (VS Code) uses under the hood.

```bash
pip install pyright
pyright my_file.py
```

Or configure it in `pyproject.toml`:

```toml
[tool.pyright]
pythonVersion = "3.10"
typeCheckingMode = "basic"  # "off", "basic", "standard", "strict"
```

### reveal_type() — debugging types

`reveal_type()` is a special function understood by type checkers (not by Python at runtime) that prints the inferred type of an expression:

```python
name = "Javi"
reveal_type(name)          # Revealed type: str

def greet(n: str) -> str:
    return f"Hello, {n}"

result = greet("Ana")
reveal_type(result)        # Revealed type: str

items = [1, 2, 3]
first = items[0]
reveal_type(first)         # Revealed type: int
```

Remove `reveal_type()` calls before committing — they cause a `NameError` at runtime.

### Strictness levels

```toml
# pyproject.toml
[tool.pyright]
typeCheckingMode = "basic"    # catches obvious errors
typeCheckingMode = "standard" # balanced — recommended for most projects
typeCheckingMode = "strict"   # everything must be annotated
```

Start with `"basic"` and increase strictness as you add more annotations.

---

## Best practices

**Annotate function signatures first** — parameters and return types give the most value for the least effort. Annotate local variables only when the type is not obvious.

**Use `X | None` instead of `Optional[X]`** — cleaner and the modern standard.

**Use `X | Y` instead of `Union[X, Y]`** — same reason.

**Use built-in generics** — `list[int]` not `List[int]`, `dict[str, int]` not `Dict[str, int]`.

**Be specific** — `list[str]` is better than `list`, which is better than `Any`.

**Use `TypedDict` for structured dicts** — never `dict[str, Any]` when you know the structure.

**Use `Protocol` for interfaces** — do not force inheritance just to satisfy a type checker.

**Use `Literal` for constrained strings** — better than a plain `str` for values like model names, directions or status codes.

**Combine with docstrings** — type hints tell you *what*, docstrings tell you *why* and *how*. Both are needed.

```python
def chunk_text(
    text: str,
    chunk_size: int = 512,
    overlap: int = 50,
    strategy: Literal["fixed", "sentence", "paragraph"] = "fixed",
) -> list[str]:
    """
    Split text into chunks for embedding.

    Args:
        text: The input text to split.
        chunk_size: Maximum number of tokens per chunk.
        overlap: Number of tokens to overlap between chunks.
        strategy: Splitting strategy to use.

    Returns:
        A list of text chunks.
    """
    ...
```

---

## Summary

- Type hints are **optional** and have **no runtime effect** — use a static checker (pyright) to enforce them.
- **Basic syntax**: `variable: type`, `def f(x: type) -> return_type`.
- **Collections** (3.9+): `list[int]`, `dict[str, int]`, `tuple[float, float]`, `set[str]`.
- **Optional**: `str | None` — value can be str or None.
- **Union**: `int | str` — value can be int or str.
- **`Any`**: opts out of type checking — use sparingly.
- **`Callable[[int, int], str]`**: type for functions passed as arguments.
- **`Literal["a", "b"]`**: restricts to specific allowed values.
- **`TypedDict`**: dict with a fixed structure and typed keys.
- **`TypeAlias`**: readable name for complex repeated types.
- **`Protocol`**: interface defined by behaviour, not inheritance.
- **`TypeVar` / `Generic`**: write functions and classes that work across types while preserving type information.
- **`reveal_type()`**: debug what type the checker infers for an expression.
- **pyright**: the recommended type checker, integrated with VS Code via Pylance.

In the next lesson we will cover code formatting with Ruff — keeping style consistent automatically.