# 09 — Classes and Object-Oriented Programming
# Exercises

# ============================================================
# Exercise 1 — Basic class
# Build a class Temperature that:
# - Stores a value in Celsius in __init__
# - Has a @property fahrenheit that returns the converted value
# - Has a @property kelvin that returns the converted value
# - Has a @classmethod from_fahrenheit(cls, f) that creates
#   a Temperature from a Fahrenheit value
# - Implements __str__ as "23.0°C" and __repr__ as
#   "Temperature(celsius=23.0)"
# - Raises ValueError if celsius < -273.15 (absolute zero)
#
# Formulas:
# F = C * 9/5 + 32
# K = C + 273.15
# ============================================================

# Your code here


# ============================================================
# Exercise 2 — Instance vs class attributes
# Build a class APIClient that:
# - Has a class attribute MAX_RETRIES = 3
# - Has a class attribute _instance_count = 0 (tracks how many
#   clients have been created)
# - __init__ receives base_url and api_key
# - Increments _instance_count on each instantiation
# - Has a @classmethod total_clients(cls) that returns the count
# - Has a @staticmethod is_valid_url(url) that returns True if
#   the url starts with "http://" or "https://"
# - Has a method get(endpoint) that returns a string like:
#   "GET {base_url}/{endpoint} (key: {api_key[:4]}...)"
#
# Test: create 3 clients, call total_clients(), test is_valid_url()
# ============================================================

# Your code here


# ============================================================
# Exercise 3 — Properties and encapsulation
# Build a class BankAccount that:
# - __init__ receives owner (str) and an optional initial
#   balance (default 0)
# - Raises ValueError if initial balance is negative
# - _balance is a private attribute
# - @property balance returns the balance
# - deposit(amount) adds amount — raises ValueError if amount <= 0
# - withdraw(amount) subtracts amount — raises ValueError if
#   amount <= 0 or amount > balance
# - transfer(amount, target_account) withdraws from self and
#   deposits into target_account atomically (if withdraw fails,
#   deposit should not happen)
# - __str__ returns "BankAccount(owner=Javi, balance=€1,234.50)"
#
# Test with valid operations and edge cases.
# ============================================================

# Your code here


# ============================================================
# Exercise 4 — Inheritance and super()
# Build a class hierarchy for a simple notification system:
#
# Notification (base class)
# - __init__(title, message, priority="normal")
# - send() — prints "Sending [priority] notification: title"
# - __str__ — "Notification: title (priority)"
#
# EmailNotification(Notification)
# - __init__(title, message, recipient, priority="normal")
# - send() — calls super().send(), then prints
#   "Email to: recipient — message"
#
# SlackNotification(Notification)
# - __init__(title, message, channel, priority="normal")
# - send() — calls super().send(), then prints
#   "Slack #channel — message"
#
# Create a list with one of each, iterate and call send().
# ============================================================

# Your code here


# ============================================================
# Exercise 5 — Composition
# Build a simple AI pipeline using composition:
#
# Prompt class
# - __init__(template: str) — template uses {variable} placeholders
# - render(**kwargs) — returns the template with variables filled in
# - __repr__ — "Prompt(template=...first 30 chars...)"
#
# Model class
# - __init__(name: str, max_tokens: int = 1000)
# - generate(prompt: str) — returns a simulated response string:
#   f"[{self.name}] Response to: {prompt[:50]}..."
#
# Chain class (uses composition — HAS A Prompt and a Model)
# - __init__(prompt: Prompt, model: Model)
# - run(**kwargs) — renders the prompt, passes it to model.generate,
#   returns the result
# - __str__ — "Chain(prompt=..., model=...)"
#
# Test: create a prompt template, a model and a chain, then run it.
# ============================================================

# Your code here


# ============================================================
# Exercise 6 — Dunder methods
# Build a class Vector that represents a 2D vector (x, y) with:
# - __init__(x, y)
# - __str__ — "Vector(3, 4)"
# - __repr__ — "Vector(x=3, y=4)"
# - __add__ — vector addition
# - __sub__ — vector subtraction
# - __mul__(scalar) — scalar multiplication
# - __eq__ — equality check
# - __len__ — returns integer magnitude (rounded)
# - __abs__ — returns exact float magnitude (sqrt(x²+y²))
# - magnitude property — same as __abs__
#
# Test all operations:
# v1 = Vector(3, 4)
# v2 = Vector(1, 2)
# v1 + v2, v1 - v2, v1 * 3, v1 == v2, len(v1), abs(v1)
# ============================================================

# Your code here


# ============================================================
# Exercise 7 — Context manager
# Part A: Build a class Timer as a context manager that:
# - Records start time on __enter__
# - Prints elapsed time on __exit__
# - Stores the elapsed time in self.elapsed
# - Returns self from __enter__ so you can do:
#   with Timer() as t:
#       ...
#   print(t.elapsed)
#
# Part B: Rewrite the same Timer using @contextmanager
# from contextlib.
#
# Test both versions with a computation.
# ============================================================

# Your code here


# ============================================================
# Exercise 8 — Dataclasses
# Define the following dataclasses for an AI model registry:
#
# ModelConfig
# - name: str
# - provider: str
# - max_tokens: int = 4096
# - temperature: float = 0.7
# - tags: list = field(default_factory=list)
# - frozen: should NOT be frozen
#
# ExperimentResult (frozen=True)
# - model_name: str
# - prompt: str
# - response: str
# - latency_ms: float
# - tokens_used: int
#
# Tasks:
# - Create 3 ModelConfig instances, add tags to each
# - Create an ExperimentResult and try to modify it
# - Sort a list of ExperimentResults by latency_ms
#   (use sorted with a key lambda since frozen dataclasses
#   don't auto-generate __lt__)
# ============================================================

from dataclasses import dataclass, field

# Your code here
