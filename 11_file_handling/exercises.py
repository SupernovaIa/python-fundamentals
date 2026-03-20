# 11 — File Handling
# Exercises

# ============================================================
# Exercise 1 — Basic read and write
# Part A: Create a file called "countries.txt" with the
# following content (one country per line):
# Spain, France, Germany, Italy, Portugal
#
# Part B: Read it back and print:
# - Total number of lines
# - Each country with its line number (1-indexed)
# - The countries sorted alphabetically
# - The longest country name
# ============================================================

# Your code here


# ============================================================
# Exercise 2 — Append and modes
# Build a simple file-based logger:
# - log(message, level="INFO") — appends a line to "app.log"
#   Format: "2026-01-15 09:30:00 [INFO] message"
# - read_logs(level=None) — reads app.log and returns a list
#   of log entries. If level is given, filter by that level.
# - clear_logs() — clears the log file
#
# Test: log several messages at different levels, then
# read and filter by "ERROR".
# ============================================================

from datetime import datetime

# Your code here


# ============================================================
# Exercise 3 — pathlib
# Given the directory structure below (create it programmatically):
#
# workspace/
#     data/
#         raw/
#         processed/
#     output/
#         reports/
#     logs/
#
# Tasks:
# - Create the full structure using pathlib (mkdir with parents)
# - Write a different text file in each leaf directory
# - List all files in workspace/ recursively using glob("**/*")
# - Print: name, parent directory, size in bytes, suffix
# - Find all .txt files and count them
# - Clean up: delete the entire workspace/ directory tree
# ============================================================

from pathlib import Path

# Your code here


# ============================================================
# Exercise 4 — CSV: reading and writing
# Part A: Create a CSV file "models.csv" with this data:
#
# name,provider,max_tokens,temperature
# gpt-4o,openai,128000,0.7
# claude-3-5-sonnet,anthropic,200000,1.0
# gemini-1.5-pro,google,1000000,0.4
# llama-3.1-70b,meta,8192,0.6
#
# Part B: Read it back using DictReader and:
# - Print each model's name and provider
# - Find the model with the highest max_tokens
# - Calculate the average temperature across all models
# - Filter and write a new CSV "high_context.csv" with only
#   models that have max_tokens > 100000
# ============================================================

import csv

# Your code here


# ============================================================
# Exercise 5 — Large file processing
# Generate a large text file with 100_000 lines:
# Each line: "line {n}: {'word ' * random(1,10)}"
#
# Then process it WITHOUT loading it fully into memory:
# - Count total lines
# - Count lines containing the word "python"
# - Find the longest line
# - Compute the average line length
# - Write all lines longer than 50 characters to "long_lines.txt"
#
# Use only iteration (for line in f:), never readlines() or read().
# ============================================================

import random

# Your code here


# ============================================================
# Exercise 6 — Error handling
# Write a robust function load_config(path) that:
# - Reads a JSON config file from the given path
# - Returns the parsed dict if successful
# - Returns {} if the file does not exist
# - Returns {} and prints a warning if JSON is malformed
# - Returns {} and prints a warning if encoding is wrong
# - Raises PermissionError if the OS denies access (don't catch this)
#
# Write a companion save_config(path, data) that:
# - Writes data as pretty-printed JSON
# - Uses atomic write (temp file + os.replace) to avoid corruption
# - Creates parent directories if they don't exist
#
# Test both functions with valid config, missing file,
# and malformed JSON.
# ============================================================

import json
import os

# Your code here


# ============================================================
# Exercise 7 — Binary files
# Part A: Write the bytes 0–255 to a binary file "bytes.bin"
# Read it back and verify all 256 bytes are present.
#
# Part B: Write a function copy_in_chunks(src, dst, chunk_size=4096)
# that copies a binary file in chunks without loading it all
# into memory. Use the walrus operator (:=) for the read loop.
#
# Test: copy "bytes.bin" to "bytes_copy.bin" and verify
# both files have identical content.
# ============================================================

# Your code here


# ============================================================
# Exercise 8 — tempfile
# Write a function pipeline(data: list[dict]) -> list[dict] that:
# 1. Writes the input data to a temporary JSON file
# 2. Reads it back and doubles any numeric values in each record
# 3. Writes the result to a second temporary file
# 4. Reads and returns the final result as a Python list
# 5. Cleans up both temporary files (even if an error occurs)
#
# Use NamedTemporaryFile or TemporaryDirectory as appropriate.
# The temp files must not exist after the function returns.
#
# Test data:
# [{"model": "gpt-4o", "tokens": 150, "latency": 320},
#  {"model": "claude", "tokens": 200, "latency": 180}]
# ============================================================

import tempfile

# Your code here
