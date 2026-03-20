# 10 — Modular Programming
# Exercises

# ============================================================
# Exercise 1 — Creating and importing modules
# Create a file called string_utils.py in the same directory
# with the following functions:
# - slugify(text) — converts "Hello World" to "hello-world"
# - truncate(text, max_length, suffix="...") — truncates text
#   and adds suffix if it exceeds max_length
# - count_words(text) — returns the number of words
# - is_palindrome(text) — ignores case and spaces
#
# Then import and test all four functions here.
# ============================================================

# Your code here (create string_utils.py first, then import)


# ============================================================
# Exercise 2 — __name__ and __main__
# Create a file called temperature.py with:
# - celsius_to_fahrenheit(c) — C to F
# - fahrenheit_to_celsius(f) — F to C
# - celsius_to_kelvin(c) — C to K
#
# Add a __main__ block that:
# - Accepts a temperature and unit from sys.argv
# - Converts to the other two units and prints all three
# - Handles missing/invalid arguments gracefully
#
# Usage: python temperature.py 100 C
# Output:
#   Celsius:    100.0°C
#   Fahrenheit: 212.0°F
#   Kelvin:     373.15K
#
# Then import celsius_to_fahrenheit here and use it.
# ============================================================

# Your code here


# ============================================================
# Exercise 3 — Package structure
# Create the following package structure:
#
# text_toolkit/
#     __init__.py        — exports clean, analyse, transform
#     cleaning.py        — strip_html(text), remove_extra_spaces(text)
#     analysis.py        — word_frequency(text), avg_word_length(text)
#     transform.py       — to_title_case(text), reverse_words(text)
#
# In __init__.py, import and re-export the six functions so
# users can do:
#   from text_toolkit import clean, analyse, transform
# or
#   from text_toolkit import strip_html, word_frequency
#
# Test all six functions here using both import styles.
# ============================================================

# Your code here


# ============================================================
# Exercise 4 — Standard library: pathlib and json
# Given a list of model configs below:
# - Create an "output" directory if it does not exist (pathlib)
# - Write the list as a JSON file at output/models.json
# - Read it back and print each model's name and max_tokens
# - Count how many models have temperature > 0.5
# - Find the model with the highest max_tokens
#
# model_configs = [
#     {"name": "gpt-4o", "provider": "openai", "max_tokens": 128000, "temperature": 0.7},
#     {"name": "claude-3-5-sonnet", "provider": "anthropic", "max_tokens": 200000, "temperature": 1.0},
#     {"name": "gemini-1.5-pro", "provider": "google", "max_tokens": 1000000, "temperature": 0.4},
#     {"name": "llama-3.1-70b", "provider": "meta", "max_tokens": 8192, "temperature": 0.6},
# ]
# ============================================================

model_configs = [
    {"name": "gpt-4o", "provider": "openai", "max_tokens": 128000, "temperature": 0.7},
    {
        "name": "claude-3-5-sonnet",
        "provider": "anthropic",
        "max_tokens": 200000,
        "temperature": 1.0,
    },
    {
        "name": "gemini-1.5-pro",
        "provider": "google",
        "max_tokens": 1000000,
        "temperature": 0.4,
    },
    {
        "name": "llama-3.1-70b",
        "provider": "meta",
        "max_tokens": 8192,
        "temperature": 0.6,
    },
]

# Your code here


# ============================================================
# Exercise 5 — collections: Counter and defaultdict
# Given the list of log entries below:
# - Use Counter to find the 3 most common log levels
# - Use Counter to find the 5 most common words across all messages
# - Use defaultdict to group entries by log level
# - Print a summary: for each level, how many entries and
#   the first message of each level
#
# logs = [
#     ("INFO", "Server started on port 8080"),
#     ("ERROR", "Connection refused to database"),
#     ("INFO", "Request received from client"),
#     ("WARNING", "Memory usage above 80%"),
#     ("ERROR", "Timeout waiting for response"),
#     ("INFO", "Request processed successfully"),
#     ("ERROR", "Failed to parse JSON response"),
#     ("INFO", "Server health check passed"),
#     ("WARNING", "Disk space below 20%"),
#     ("INFO", "Cache cleared successfully"),
# ]
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

# Your code here


# ============================================================
# Exercise 6 — functools: lru_cache and partial
# Part A: Write a recursive function fib(n) that computes the
# nth Fibonacci number. Decorate it with @lru_cache.
# - Compute fib(40) and print the result
# - Print the cache info with fib.cache_info()
# - Call fib(40) again and confirm it is instant (cache hit)
#
# Part B: You have the function below:
#   def format_number(value, decimals, prefix="", suffix=""):
#       return f"{prefix}{value:.{decimals}f}{suffix}"
#
# Use partial to create:
# - format_price(value) → "€1,234.57" (2 decimals, € prefix)
# - format_percentage(value) → "15.67%" (2 decimals, % suffix)
# - format_temperature(value) → "23.5°C" (1 decimal, °C suffix)
# Test each one.
# ============================================================

from functools import lru_cache, partial


def format_number(value, decimals, prefix="", suffix=""):
    return f"{prefix}{value:,.{decimals}f}{suffix}"


# Your code here


# ============================================================
# Exercise 7 — Named tuples
# Define the following named tuples:
#
# APIResponse — fields: status_code, body, latency_ms, model
# TokenUsage  — fields: prompt_tokens, completion_tokens, total_tokens
#
# - Create 3 APIResponse instances simulating model calls
# - Create a TokenUsage for each using the formula:
#   total = prompt + completion
# - Sort the responses by latency_ms (ascending)
# - Print a summary table:
#   Model          | Status | Latency | Total tokens
#   ---------------|--------|---------|-------------
#   gpt-4o         |    200 |  320ms  |          450
#   ...
# ============================================================

from collections import namedtuple

# Your code here


# ============================================================
# Exercise 8 — itertools
# Use itertools (no manual loops where itertools works better):
#
# Part A: Given multiple lists of embeddings (each a list of
# floats), use chain to flatten them into a single list.
#
# Part B: Given a list of model names and a list of prompts,
# use product to generate all (model, prompt) combinations
# and print them.
#
# Part C: Given a large range (1 to 10_000_000), use islice
# to take only the first 10 even numbers — without building
# the full list in memory.
#
# embeddings = [[0.1, 0.2, 0.3], [0.4, 0.5], [0.6, 0.7, 0.8, 0.9]]
# models = ["gpt-4o", "claude-3-5-sonnet", "gemini-1.5-pro"]
# prompts = ["Summarise this", "Translate to Spanish"]
# ============================================================

import itertools

embeddings = [[0.1, 0.2, 0.3], [0.4, 0.5], [0.6, 0.7, 0.8, 0.9]]
models = ["gpt-4o", "claude-3-5-sonnet", "gemini-1.5-pro"]
prompts = ["Summarise this", "Translate to Spanish"]

# Your code here
