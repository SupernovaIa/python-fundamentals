# 11 — File Handling
# Solutions

import csv
import json
import os
import random
import tempfile
from datetime import datetime
from pathlib import Path

BASE = Path(__file__).parent

# ============================================================
# Exercise 1 — Basic read and write
# ============================================================

countries_path = BASE / "countries.txt"

# Part A: write
with open(countries_path, "w") as f:
    for country in ["Spain", "France", "Germany", "Italy", "Portugal"]:
        f.write(country + "\n")

# Part B: read
with open(countries_path) as f:
    lines = [line.strip() for line in f]

print(f"Total lines: {len(lines)}")
for i, country in enumerate(lines, start=1):
    print(f"{i}. {country}")
print("Sorted:", sorted(lines))
print("Longest:", max(lines, key=len))


# ============================================================
# Exercise 2 — Append and modes
# ============================================================

log_path = BASE / "app.log"

def log(message: str, level: str = "INFO") -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_path, "a") as f:
        f.write(f"{timestamp} [{level}] {message}\n")

def read_logs(level: str | None = None) -> list[str]:
    try:
        with open(log_path) as f:
            entries = [line.strip() for line in f if line.strip()]
        if level:
            entries = [e for e in entries if f"[{level}]" in e]
        return entries
    except FileNotFoundError:
        return []

def clear_logs() -> None:
    with open(log_path, "w"):
        pass  # truncate


clear_logs()
log("Server started")
log("Connection refused", "ERROR")
log("Request received")
log("Memory warning", "WARNING")
log("Timeout exceeded", "ERROR")

print("\nAll logs:")
for entry in read_logs():
    print(" ", entry)

print("\nERROR only:")
for entry in read_logs("ERROR"):
    print(" ", entry)


# ============================================================
# Exercise 3 — pathlib
# ============================================================

workspace = BASE / "workspace"

# Create structure
for leaf in [
    workspace / "data" / "raw",
    workspace / "data" / "processed",
    workspace / "output" / "reports",
    workspace / "logs",
]:
    leaf.mkdir(parents=True, exist_ok=True)
    (leaf / "readme.txt").write_text(f"Directory: {leaf.name}\n")

# List all files recursively
print("\nAll files in workspace:")
for f in workspace.glob("**/*"):
    if f.is_file():
        print(f"  name={f.name}, parent={f.parent.name}, "
              f"size={f.stat().st_size}B, suffix={f.suffix!r}")

txt_count = len(list(workspace.glob("**/*.txt")))
print(f"\n.txt files: {txt_count}")

# Clean up
import shutil
shutil.rmtree(workspace)
print("workspace removed.")


# ============================================================
# Exercise 4 — CSV: reading and writing
# ============================================================

csv_data = [
    {"name": "gpt-4o", "provider": "openai", "max_tokens": "128000", "temperature": "0.7"},
    {"name": "claude-3-5-sonnet", "provider": "anthropic", "max_tokens": "200000", "temperature": "1.0"},
    {"name": "gemini-1.5-pro", "provider": "google", "max_tokens": "1000000", "temperature": "0.4"},
    {"name": "llama-3.1-70b", "provider": "meta", "max_tokens": "8192", "temperature": "0.6"},
]

models_csv = BASE / "models.csv"
high_ctx_csv = BASE / "high_context.csv"

# Part A: write
with open(models_csv, "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "provider", "max_tokens", "temperature"])
    writer.writeheader()
    writer.writerows(csv_data)

# Part B: read back
with open(models_csv, newline="") as f:
    reader = list(csv.DictReader(f))

for row in reader:
    print(f"{row['name']} ({row['provider']})")

best = max(reader, key=lambda r: int(r["max_tokens"]))
print(f"Highest context: {best['name']}")

avg_temp = sum(float(r["temperature"]) for r in reader) / len(reader)
print(f"Avg temperature: {avg_temp:.2f}")

high_ctx = [r for r in reader if int(r["max_tokens"]) > 100_000]
with open(high_ctx_csv, "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=reader[0].keys())
    writer.writeheader()
    writer.writerows(high_ctx)


# ============================================================
# Exercise 5 — Large file processing
# ============================================================

random.seed(42)
words = ["python", "ai", "llm", "agent", "vector", "model", "data", "code"]
large_file = BASE / "large.txt"

with open(large_file, "w") as f:
    for n in range(1, 100_001):
        word_count = random.randint(1, 10)
        line_words = " ".join(random.choices(words, k=word_count))
        f.write(f"line {n}: {line_words}\n")

total_lines = 0
python_lines = 0
longest = ""
total_len = 0

with open(large_file) as f:
    with open(BASE / "long_lines.txt", "w") as out:
        for line in f:
            total_lines += 1
            total_len += len(line)
            if "python" in line:
                python_lines += 1
            if len(line) > len(longest):
                longest = line
            if len(line.rstrip()) > 50:
                out.write(line)

print(f"\nTotal lines: {total_lines}")
print(f"Lines with 'python': {python_lines}")
print(f"Longest line ({len(longest)} chars): {longest[:60].rstrip()}")
print(f"Avg line length: {total_len / total_lines:.1f} chars")

large_file.unlink()
(BASE / "long_lines.txt").unlink(missing_ok=True)


# ============================================================
# Exercise 6 — Error handling
# ============================================================

def load_config(path: Path) -> dict:
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError as e:
        print(f"Warning: malformed JSON in {path}: {e}")
        return {}
    except UnicodeDecodeError as e:
        print(f"Warning: encoding error in {path}: {e}")
        return {}
    # PermissionError is intentionally NOT caught — it should propagate


def save_config(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(".tmp")
    try:
        with open(tmp, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
        os.replace(tmp, path)
    except Exception:
        tmp.unlink(missing_ok=True)
        raise


config_path = BASE / "config.json"
save_config(config_path, {"model": "gpt-4o", "temperature": 0.7})
print(load_config(config_path))
print(load_config(BASE / "nonexistent.json"))   # {}

bad_json = BASE / "bad.json"
bad_json.write_text("{not valid json")
print(load_config(bad_json))                    # {}, warning printed

config_path.unlink(missing_ok=True)
bad_json.unlink(missing_ok=True)


# ============================================================
# Exercise 7 — Binary files
# ============================================================

bytes_file = BASE / "bytes.bin"
bytes_copy = BASE / "bytes_copy.bin"

# Part A: write 0–255 and verify
with open(bytes_file, "wb") as f:
    f.write(bytes(range(256)))

with open(bytes_file, "rb") as f:
    data = f.read()
assert list(data) == list(range(256)), "Mismatch!"
print(f"All 256 bytes present: {len(data) == 256}")


# Part B: copy in chunks using walrus operator
def copy_in_chunks(src: Path, dst: Path, chunk_size: int = 4096) -> None:
    with open(src, "rb") as fsrc, open(dst, "wb") as fdst:
        while chunk := fsrc.read(chunk_size):
            fdst.write(chunk)


copy_in_chunks(bytes_file, bytes_copy)

assert bytes_file.read_bytes() == bytes_copy.read_bytes(), "Files differ!"
print("Files are identical.")

bytes_file.unlink()
bytes_copy.unlink()


# ============================================================
# Exercise 8 — tempfile
# ============================================================

def pipeline(data: list[dict]) -> list[dict]:
    tmp1 = tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False)
    tmp2 = tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False)
    path1 = Path(tmp1.name)
    path2 = Path(tmp2.name)
    try:
        # Step 1: write input to temp file
        with open(path1, "w") as f:
            json.dump(data, f)

        # Step 2: read back, double numeric values
        with open(path1) as f:
            loaded = json.load(f)

        doubled = [
            {k: v * 2 if isinstance(v, (int, float)) else v for k, v in record.items()}
            for record in loaded
        ]

        # Step 3: write result to second temp file
        with open(path2, "w") as f:
            json.dump(doubled, f)

        # Step 4: read and return final result
        with open(path2) as f:
            return json.load(f)
    finally:
        path1.unlink(missing_ok=True)
        path2.unlink(missing_ok=True)


test_data = [
    {"model": "gpt-4o", "tokens": 150, "latency": 320},
    {"model": "claude", "tokens": 200, "latency": 180},
]
result = pipeline(test_data)
print(result)
