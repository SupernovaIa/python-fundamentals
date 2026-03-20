# 12 — Type Hints
# Solutions

from typing import Any, Callable, Literal, Protocol, TypeAlias, TypeVar
from typing import TypedDict, NotRequired, Generic

# ============================================================
# Exercise 1 — Basic annotations
# ============================================================

def calculate_bmi(weight: float, height: float) -> float:
    return weight / (height**2)


def greet_user(name: str, title: str | None = None) -> str:
    if title:
        return f"Hello, {title} {name}"
    return f"Hello, {name}"


def count_occurrences(text: str, char: str) -> int:
    return text.lower().count(char.lower())


def flatten(nested: list[list[Any]]) -> list[Any]:
    result: list[Any] = []
    for sublist in nested:
        result.extend(sublist)
    return result


max_retries: int = 3
base_url: str = "https://api.example.com"
debug_mode: bool = False
allowed_models: list[str] = ["gpt-4o", "claude-3-5-sonnet", "gemini-1.5-pro"]


# ============================================================
# Exercise 2 — Optional and Union
# ============================================================

def find_by_id(records: list[dict[str, Any]], target_id: int) -> dict[str, Any] | None:
    for record in records:
        if record["id"] == target_id:
            return record
    return None


def parse_number(raw: str | int | float) -> float | None:
    try:
        return float(raw)
    except (ValueError, TypeError):
        return None


def merge_configs(
    base: dict[str, str | int | bool],
    override: dict[str, str | int | bool] | None,
) -> dict[str, str | int | bool]:
    result = dict(base)
    if override:
        result.update(override)
    return result


# ============================================================
# Exercise 3 — Callable
# ============================================================

def apply_twice(func: Callable[[str], str], value: str) -> str:
    return func(func(value))


def pipeline(steps: list[Callable[[str], str]], data: str) -> str:
    for step in steps:
        data = step(data)
    return data


def retry(
    func: Callable[[], str],
    max_attempts: int,
    on_failure: Callable[[Exception], None] | None = None,
) -> str | None:
    for _ in range(max_attempts):
        try:
            return func()
        except Exception as e:
            if on_failure:
                on_failure(e)
    return None


# ============================================================
# Exercise 4 — Literal
# ============================================================

LogLevel: TypeAlias = Literal["debug", "info", "warning", "error", "critical"]
SortOrder: TypeAlias = Literal["asc", "desc"]
ModelProvider: TypeAlias = Literal["openai", "anthropic", "google", "meta"]
ChunkStrategy: TypeAlias = Literal["fixed", "sentence", "paragraph", "semantic"]


def log(message: str, level: LogLevel) -> None:
    print(f"[{level.upper()}] {message}")


def sort_records(
    records: list[dict[str, Any]], key: str, order: SortOrder
) -> list[dict[str, Any]]:
    reverse = order == "desc"
    return sorted(records, key=lambda r: r[key], reverse=reverse)


def get_model_config(provider: ModelProvider) -> dict[str, float | int]:
    configs: dict[str, dict[str, float | int]] = {
        "openai": {"max_tokens": 128000, "temperature": 0.7},
        "anthropic": {"max_tokens": 200000, "temperature": 1.0},
        "google": {"max_tokens": 1000000, "temperature": 0.4},
        "meta": {"max_tokens": 8192, "temperature": 0.6},
    }
    return configs[provider]


# ============================================================
# Exercise 5 — TypedDict
# ============================================================

class ModelConfig(TypedDict):
    name: str
    provider: str
    max_tokens: int
    temperature: float
    system_prompt: NotRequired[str]


class APIResponse(TypedDict):
    status_code: int
    body: str
    model: str
    tokens_used: int
    latency_ms: float
    error: NotRequired[str]


def build_config(
    name: str,
    provider: str,
    max_tokens: int,
    temperature: float,
    system_prompt: str | None = None,
) -> ModelConfig:
    config: ModelConfig = {
        "name": name,
        "provider": provider,
        "max_tokens": max_tokens,
        "temperature": temperature,
    }
    if system_prompt:
        config["system_prompt"] = system_prompt
    return config


def is_successful(response: APIResponse) -> bool:
    return 200 <= response["status_code"] < 300


def extract_error(response: APIResponse) -> str | None:
    return response.get("error")


# ============================================================
# Exercise 6 — Protocol
# ============================================================

class TextSplitter(Protocol):
    def split(self, text: str, chunk_size: int) -> list[str]: ...


class VectorStore(Protocol):
    def add(self, id: str, vector: list[float], metadata: dict[str, str]) -> None: ...
    def search(self, query: list[float], top_k: int) -> list[str]: ...


class LLM(Protocol):
    def generate(self, prompt: str, max_tokens: int) -> str: ...
    def count_tokens(self, text: str) -> int: ...


def build_rag_pipeline(
    splitter: TextSplitter,
    store: VectorStore,
    llm: LLM,
    text: str,
    query: str,
) -> str:
    chunks = splitter.split(text, chunk_size=256)
    for i, chunk in enumerate(chunks):
        store.add(str(i), [0.0] * 10, {"text": chunk})
    results = store.search([0.0] * 10, top_k=3)
    context = "\n".join(results)
    prompt = f"Context:\n{context}\n\nQuestion: {query}"
    return llm.generate(prompt, max_tokens=512)


# ============================================================
# Exercise 7 — TypeVar and Generic
# ============================================================

T = TypeVar("T")
K = TypeVar("K")
V = TypeVar("V")


class Queue(Generic[T]):
    """A generic FIFO queue."""

    def __init__(self) -> None:
        self._items: list[T] = []

    def enqueue(self, item: T) -> None:
        self._items.append(item)

    def dequeue(self) -> T:
        if not self._items:
            raise IndexError("dequeue from empty Queue")
        return self._items.pop(0)

    def peek(self) -> T | None:
        return self._items[0] if self._items else None

    def is_empty(self) -> bool:
        return len(self._items) == 0

    def __len__(self) -> int:
        return len(self._items)


def zip_to_dict(keys: list[K], values: list[V]) -> dict[K, V]:
    return dict(zip(keys, values))


def batch(items: list[T], size: int) -> list[list[T]]:
    return [items[i : i + size] for i in range(0, len(items), size)]


# ============================================================
# Exercise 8 — Full annotation review
# ============================================================

class RAGPipeline:
    """A simple retrieval-augmented generation pipeline."""

    DEFAULT_CHUNK_SIZE: int = 512
    DEFAULT_TOP_K: int = 3

    def __init__(self, model_name: str, provider: str, max_tokens: int = 1024) -> None:
        self.model_name: str = model_name
        self.provider: str = provider
        self.max_tokens: int = max_tokens
        self.chunks: list[str] = []
        self.metadata: dict[int, str] = {}
        self._call_count: int = 0

    def ingest(self, text: str, source: str | None = None) -> int:
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

    def retrieve(self, query: str, top_k: int | None = None) -> list[str]:
        """Return top_k chunks that contain any word from the query."""
        k = top_k or self.DEFAULT_TOP_K
        query_words = set(query.lower().split())
        scored: list[tuple[str, int]] = [
            (chunk, len(query_words & set(chunk.lower().split())))
            for chunk in self.chunks
        ]
        scored.sort(key=lambda x: x[1], reverse=True)
        return [chunk for chunk, _ in scored[:k]]

    def generate(self, query: str, top_k: int | None = None) -> str:
        """Retrieve context and simulate a model response."""
        context_chunks = self.retrieve(query, top_k)
        self._call_count += 1
        context = "\n---\n".join(context_chunks)
        return (
            f"[{self.model_name}] Based on context:\n{context}\n\nAnswer: <generated>"
        )

    def stats(self) -> dict[str, str | int]:
        """Return pipeline statistics."""
        return {
            "model": self.model_name,
            "provider": self.provider,
            "chunks_stored": len(self.chunks),
            "calls_made": self._call_count,
        }
