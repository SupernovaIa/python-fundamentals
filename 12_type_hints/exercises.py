# 12 — Type Hints
# Exercises
#
# For these exercises, run pyright after writing each function
# to verify your annotations are correct:
#   pyright 12_type_hints_exercises.py

from typing import Any, Callable, Literal, Protocol, TypeAlias, TypeVar
from typing import TypedDict, NotRequired, Generic


# ============================================================
# Exercise 1 — Basic annotations
# Add complete type annotations to all functions and variables
# below. Do not change any logic — only add type hints.
# Run pyright to verify there are no errors.
# ============================================================


def calculate_bmi(weight, height):
    return weight / (height**2)


def greet_user(name, title=None):
    if title:
        return f"Hello, {title} {name}"
    return f"Hello, {name}"


def count_occurrences(text, char):
    return text.lower().count(char.lower())


def flatten(nested):
    result = []
    for sublist in nested:
        result.extend(sublist)
    return result


max_retries = 3
base_url = "https://api.example.com"
debug_mode = False
allowed_models = ["gpt-4o", "claude-3-5-sonnet", "gemini-1.5-pro"]


# ============================================================
# Exercise 2 — Optional and Union
# Annotate the functions below using | None and | syntax.
# Each function's docstring describes the intended behaviour.
# ============================================================


def find_by_id(records, target_id):
    """
    Search a list of dicts for a record with the given id.
    Returns the record dict if found, None otherwise.
    records: list of dicts with at least an "id" key (int)
    target_id: int
    """
    for record in records:
        if record["id"] == target_id:
            return record
    return None


def parse_number(raw):
    """
    Try to convert raw (str or int or float) to float.
    Return the float if successful, None if conversion fails.
    """
    try:
        return float(raw)
    except (ValueError, TypeError):
        return None


def merge_configs(base, override):
    """
    Merge two config dicts. override may be None (no override).
    Returns a new dict with override values taking precedence.
    Both dicts have str keys and values that are str, int or bool.
    """
    result = dict(base)
    if override:
        result.update(override)
    return result


# ============================================================
# Exercise 3 — Callable
# Annotate these higher-order functions with Callable types.
# ============================================================


def apply_twice(func, value):
    """Apply func to value, then apply func to the result."""
    return func(func(value))


def pipeline(steps, data):
    """
    Apply a list of string-to-string transformation functions
    to data in sequence. Return the final result.
    """
    for step in steps:
        data = step(data)
    return data


def retry(func, max_attempts, on_failure=None):
    """
    Call func() up to max_attempts times.
    If it raises an exception, call on_failure(error) if provided.
    Return the result of the first successful call, or None.
    func: takes no arguments, returns str
    on_failure: takes an Exception, returns None — optional
    """
    for _ in range(max_attempts):
        try:
            return func()
        except Exception as e:
            if on_failure:
                on_failure(e)
    return None


# ============================================================
# Exercise 4 — Literal
# Define Literal types for the constrained parameters below
# and annotate the functions.
# ============================================================

# Define these as TypeAliases using Literal:
# - LogLevel: "debug", "info", "warning", "error", "critical"
# - SortOrder: "asc", "desc"
# - ModelProvider: "openai", "anthropic", "google", "meta"
# - ChunkStrategy: "fixed", "sentence", "paragraph", "semantic"

# Your TypeAliases here


def log(message, level):
    """Log a message at the given level."""
    print(f"[{level.upper()}] {message}")


def sort_records(records, key, order):
    """Sort a list of dicts by key in the given order."""
    reverse = order == "desc"
    return sorted(records, key=lambda r: r[key], reverse=reverse)


def get_model_config(provider):
    """Return a base config dict for the given provider."""
    configs = {
        "openai": {"max_tokens": 128000, "temperature": 0.7},
        "anthropic": {"max_tokens": 200000, "temperature": 1.0},
        "google": {"max_tokens": 1000000, "temperature": 0.4},
        "meta": {"max_tokens": 8192, "temperature": 0.6},
    }
    return configs[provider]


# ============================================================
# Exercise 5 — TypedDict
# Define TypedDicts for the following structures and annotate
# the functions that use them.
# ============================================================

# Define a TypedDict called ModelConfig with:
# - name: str (required)
# - provider: str (required)
# - max_tokens: int (required)
# - temperature: float (required)
# - system_prompt: str (optional — use NotRequired)

# Define a TypedDict called APIResponse with:
# - status_code: int (required)
# - body: str (required)
# - model: str (required)
# - tokens_used: int (required)
# - latency_ms: float (required)
# - error: str (optional — use NotRequired)

# Your TypedDicts here


def build_config(name, provider, max_tokens, temperature, system_prompt=None):
    """Build a ModelConfig dict."""
    config = {
        "name": name,
        "provider": provider,
        "max_tokens": max_tokens,
        "temperature": temperature,
    }
    if system_prompt:
        config["system_prompt"] = system_prompt
    return config


def is_successful(response):
    """Return True if the response has a 2xx status code."""
    return 200 <= response["status_code"] < 300


def extract_error(response):
    """Return the error message from a response, or None."""
    return response.get("error")


# ============================================================
# Exercise 6 — Protocol
# Define Protocols for these interfaces and annotate the
# functions that consume them.
# ============================================================

# Define a Protocol called TextSplitter with:
# - split(text: str, chunk_size: int) -> list[str]

# Define a Protocol called VectorStore with:
# - add(id: str, vector: list[float], metadata: dict[str, str]) -> None
# - search(query: list[float], top_k: int) -> list[str]

# Define a Protocol called LLM with:
# - generate(prompt: str, max_tokens: int) -> str
# - count_tokens(text: str) -> int

# Your Protocols here


def build_rag_pipeline(splitter, store, llm, text, query):
    """
    Simple RAG pipeline:
    1. Split text into chunks using splitter
    2. Add chunks to store (use chunk index as id, dummy vector)
    3. Search store for top 3 relevant chunks
    4. Build prompt from retrieved chunks + query
    5. Generate response with llm
    Return the generated response.
    """
    chunks = splitter.split(text, chunk_size=256)
    for i, chunk in enumerate(chunks):
        store.add(str(i), [0.0] * 10, {"text": chunk})
    results = store.search([0.0] * 10, top_k=3)
    context = "\n".join(results)
    prompt = f"Context:\n{context}\n\nQuestion: {query}"
    return llm.generate(prompt, max_tokens=512)


# ============================================================
# Exercise 7 — TypeVar and Generic
# Implement the generic classes and functions below.
# ============================================================

T = TypeVar("T")
K = TypeVar("K")
V = TypeVar("V")


class Queue(Generic[T]):
    """
    A generic FIFO queue.
    Implement:
    - enqueue(item: T) -> None
    - dequeue() -> T  (raises IndexError if empty)
    - peek() -> T | None  (returns front item without removing)
    - is_empty() -> bool
    - __len__() -> int
    """

    # Your implementation here
    pass


def zip_to_dict(keys, values):
    """
    Combine a list of keys and a list of values into a dict.
    The return type should preserve K and V type information.
    Example: zip_to_dict(["a", "b"], [1, 2]) -> {"a": 1, "b": 2}
    """
    return dict(zip(keys, values))


def batch(items, size):
    """
    Split items into batches of the given size.
    The return type should be list[list[T]].
    Example: batch([1,2,3,4,5], 2) -> [[1,2],[3,4],[5]]
    """
    return [items[i : i + size] for i in range(0, len(items), size)]


# ============================================================
# Exercise 8 — Full annotation review
# The class below is completely unannotated. Add full type
# annotations to all attributes, parameters and return types.
# Then run pyright in strict mode and fix all errors.
#   pyright --outputjson 12_type_hints_exercises.py
# ============================================================


class RAGPipeline:
    """A simple retrieval-augmented generation pipeline."""

    DEFAULT_CHUNK_SIZE = 512
    DEFAULT_TOP_K = 3

    def __init__(self, model_name, provider, max_tokens=1024):
        self.model_name = model_name
        self.provider = provider
        self.max_tokens = max_tokens
        self.chunks = []
        self.metadata = {}
        self._call_count = 0

    def ingest(self, text, source=None):
        """Split text into chunks and store with optional source metadata."""
        words = text.split()
        size = self.DEFAULT_CHUNK_SIZE
        new_chunks = [" ".join(words[i : i + size]) for i in range(0, len(words), size)]
        for chunk in new_chunks:
            idx = len(self.chunks)
            self.chunks.append(chunk)
            if source:
                self.metadata[idx] = source
        return len(new_chunks)

    def retrieve(self, query, top_k=None):
        """Return top_k chunks that contain any word from the query."""
        k = top_k or self.DEFAULT_TOP_K
        query_words = set(query.lower().split())
        scored = [
            (chunk, len(query_words & set(chunk.lower().split())))
            for chunk in self.chunks
        ]
        scored.sort(key=lambda x: x[1], reverse=True)
        return [chunk for chunk, _ in scored[:k]]

    def generate(self, query, top_k=None):
        """Retrieve context and simulate a model response."""
        context_chunks = self.retrieve(query, top_k)
        self._call_count += 1
        context = "\n---\n".join(context_chunks)
        return (
            f"[{self.model_name}] Based on context:\n{context}\n\nAnswer: <generated>"
        )

    def stats(self):
        """Return pipeline statistics."""
        return {
            "model": self.model_name,
            "provider": self.provider,
            "chunks_stored": len(self.chunks),
            "calls_made": self._call_count,
        }
