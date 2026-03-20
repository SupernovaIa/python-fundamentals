# 10 — Modular Programming
# Solutions
#
# Note: Exercises 1, 2 and 3 require creating external files.
# The files are created inline below using pathlib.Path.write_text
# so this solutions.py is self-contained and runnable as-is.

import itertools
import json
from collections import Counter, defaultdict
from functools import lru_cache, partial
from pathlib import Path
from collections import namedtuple

# ============================================================
# Exercise 1 — Creating and importing modules
# ============================================================

# Create string_utils.py in the same directory
_string_utils_code = '''
def slugify(text: str) -> str:
    return text.lower().strip().replace(" ", "-")

def truncate(text: str, max_length: int, suffix: str = "...") -> str:
    if len(text) <= max_length:
        return text
    return text[:max_length - len(suffix)] + suffix

def count_words(text: str) -> int:
    return len(text.split())

def is_palindrome(text: str) -> bool:
    cleaned = text.lower().replace(" ", "")
    return cleaned == cleaned[::-1]
'''

Path(__file__).parent.joinpath("string_utils.py").write_text(_string_utils_code.strip())

from string_utils import slugify, truncate, count_words, is_palindrome  # noqa: E402

print(slugify("Hello World"))                       # hello-world
print(truncate("Python is great", 10))              # Python is...
print(count_words("The quick brown fox"))           # 4
print(is_palindrome("A man a plan a canal Panama")) # True


# ============================================================
# Exercise 2 — __name__ and __main__
# ============================================================

_temperature_code = '''
import sys

def celsius_to_fahrenheit(c: float) -> float:
    return c * 9 / 5 + 32

def fahrenheit_to_celsius(f: float) -> float:
    return (f - 32) * 5 / 9

def celsius_to_kelvin(c: float) -> float:
    return c + 273.15

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python temperature.py <value> <unit (C/F/K)>")
        sys.exit(1)
    try:
        value = float(sys.argv[1])
        unit = sys.argv[2].upper()
    except ValueError:
        print("Error: value must be a number.")
        sys.exit(1)

    if unit == "C":
        c = value
    elif unit == "F":
        c = fahrenheit_to_celsius(value)
    else:
        print("Error: unit must be C or F.")
        sys.exit(1)

    print(f"Celsius:    {c:.1f}°C")
    print(f"Fahrenheit: {celsius_to_fahrenheit(c):.1f}°F")
    print(f"Kelvin:     {celsius_to_kelvin(c):.2f}K")
'''

Path(__file__).parent.joinpath("temperature.py").write_text(_temperature_code.strip())

from temperature import celsius_to_fahrenheit  # noqa: E402

print(celsius_to_fahrenheit(100))   # 212.0


# ============================================================
# Exercise 3 — Package structure
# ============================================================

pkg = Path(__file__).parent / "text_toolkit"
pkg.mkdir(exist_ok=True)

(pkg / "cleaning.py").write_text('''
import re

def strip_html(text: str) -> str:
    return re.sub(r"<[^>]+>", "", text)

def remove_extra_spaces(text: str) -> str:
    return " ".join(text.split())
'''.strip())

(pkg / "analysis.py").write_text('''
from collections import Counter

def word_frequency(text: str) -> dict[str, int]:
    return dict(Counter(text.lower().split()))

def avg_word_length(text: str) -> float:
    words = text.split()
    return sum(len(w) for w in words) / len(words) if words else 0.0
'''.strip())

(pkg / "transform.py").write_text('''
def to_title_case(text: str) -> str:
    return text.title()

def reverse_words(text: str) -> str:
    return " ".join(text.split()[::-1])
'''.strip())

(pkg / "__init__.py").write_text('''
from text_toolkit.cleaning import strip_html, remove_extra_spaces
from text_toolkit.analysis import word_frequency, avg_word_length
from text_toolkit.transform import to_title_case, reverse_words

clean = type("clean", (), {"strip_html": staticmethod(strip_html),
                            "remove_extra_spaces": staticmethod(remove_extra_spaces)})()
analyse = type("analyse", (), {"word_frequency": staticmethod(word_frequency),
                                "avg_word_length": staticmethod(avg_word_length)})()
transform = type("transform", (), {"to_title_case": staticmethod(to_title_case),
                                    "reverse_words": staticmethod(reverse_words)})()
'''.strip())

from text_toolkit import strip_html, word_frequency, to_title_case  # noqa: E402
from text_toolkit import clean, analyse, transform                   # noqa: E402

print(strip_html("<p>Hello <b>world</b></p>"))          # Hello world
print(word_frequency("the cat sat on the mat"))
print(to_title_case("hello world"))                     # Hello World
print(clean.remove_extra_spaces("too  many   spaces"))
print(analyse.avg_word_length("Python is great"))
print(transform.reverse_words("hello world"))


# ============================================================
# Exercise 4 — Standard library: pathlib and json
# ============================================================

model_configs = [
    {"name": "gpt-4o", "provider": "openai", "max_tokens": 128000, "temperature": 0.7},
    {"name": "claude-3-5-sonnet", "provider": "anthropic", "max_tokens": 200000, "temperature": 1.0},
    {"name": "gemini-1.5-pro", "provider": "google", "max_tokens": 1000000, "temperature": 0.4},
    {"name": "llama-3.1-70b", "provider": "meta", "max_tokens": 8192, "temperature": 0.6},
]

output_dir = Path(__file__).parent / "output"
output_dir.mkdir(exist_ok=True)

models_path = output_dir / "models.json"
with open(models_path, "w") as f:
    json.dump(model_configs, f, indent=2)

with open(models_path) as f:
    loaded = json.load(f)

for m in loaded:
    print(f"{m['name']}: {m['max_tokens']} tokens")

high_temp = sum(1 for m in loaded if m["temperature"] > 0.5)
print(f"Models with temperature > 0.5: {high_temp}")

best = max(loaded, key=lambda m: m["max_tokens"])
print(f"Highest context: {best['name']} ({best['max_tokens']})")


# ============================================================
# Exercise 5 — collections: Counter and defaultdict
# ============================================================

logs = [
    ("INFO", "Server started on port 8080"),
    ("ERROR", "Connection refused to database"),
    ("INFO", "Request received from client"),
    ("WARNING", "Memory usage above 80%"),
    ("ERROR", "Timeout waiting for response"),
    ("INFO", "Request processed successfully"),
    ("ERROR", "Failed to parse JSON response"),
    ("INFO", "Server health check passed"),
    ("WARNING", "Disk space below 20%"),
    ("INFO", "Cache cleared successfully"),
]

# 3 most common log levels
level_counts = Counter(level for level, _ in logs)
print("Top 3 levels:", level_counts.most_common(3))

# 5 most common words across all messages
all_words = " ".join(msg for _, msg in logs).lower().split()
word_counts = Counter(all_words)
print("Top 5 words:", word_counts.most_common(5))

# Group by level using defaultdict
by_level: dict[str, list[str]] = defaultdict(list)
for level, msg in logs:
    by_level[level].append(msg)

for level, messages in by_level.items():
    print(f"{level}: {len(messages)} entries | first: '{messages[0]}'")


# ============================================================
# Exercise 6 — functools: lru_cache and partial
# ============================================================

@lru_cache(maxsize=None)
def fib(n: int) -> int:
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


print(fib(40))
print(fib.cache_info())
print(fib(40))              # instant cache hit


def format_number(value: float, decimals: int, prefix: str = "", suffix: str = "") -> str:
    return f"{prefix}{value:,.{decimals}f}{suffix}"


format_price = partial(format_number, decimals=2, prefix="€")
format_percentage = partial(format_number, decimals=2, suffix="%")
format_temperature = partial(format_number, decimals=1, suffix="°C")

print(format_price(1234.567))       # €1,234.57
print(format_percentage(15.678))    # 15.68%
print(format_temperature(23.5))     # 23.5°C


# ============================================================
# Exercise 7 — Named tuples
# ============================================================

APIResponse = namedtuple("APIResponse", ["status_code", "body", "latency_ms", "model"])
TokenUsage = namedtuple("TokenUsage", ["prompt_tokens", "completion_tokens", "total_tokens"])

responses = [
    APIResponse(200, "...", 320.0, "gpt-4o"),
    APIResponse(200, "...", 180.0, "claude-3-5-sonnet"),
    APIResponse(200, "...", 540.0, "gemini-1.5-pro"),
]

usages = [
    TokenUsage(200, 250, 200 + 250),
    TokenUsage(180, 200, 180 + 200),
    TokenUsage(220, 290, 220 + 290),
]

sorted_responses = sorted(responses, key=lambda r: r.latency_ms)

print(f"{'Model':<22} | {'Status':>6} | {'Latency':>8} | {'Total tokens':>12}")
print("-" * 58)
for r, u in zip(sorted_responses, sorted(usages, key=lambda u: u.total_tokens)):
    print(f"{r.model:<22} | {r.status_code:>6} | {r.latency_ms:>6.0f}ms | {u.total_tokens:>12}")


# ============================================================
# Exercise 8 — itertools
# ============================================================

embeddings = [[0.1, 0.2, 0.3], [0.4, 0.5], [0.6, 0.7, 0.8, 0.9]]
models = ["gpt-4o", "claude-3-5-sonnet", "gemini-1.5-pro"]
prompts = ["Summarise this", "Translate to Spanish"]

# Part A: flatten embeddings with chain
flat_embeddings = list(itertools.chain.from_iterable(embeddings))
print("Flat embeddings:", flat_embeddings)

# Part B: all (model, prompt) combinations with product
for model, prompt in itertools.product(models, prompts):
    print(f"  {model} | {prompt}")

# Part C: first 10 even numbers from 1..10_000_000 using islice
evens = itertools.islice((n for n in range(1, 10_000_001) if n % 2 == 0), 10)
print("First 10 evens:", list(evens))
