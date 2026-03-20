# 09 — Classes
# Solutions

import math
import time
from contextlib import contextmanager
from dataclasses import dataclass, field

# ============================================================
# Exercise 1 — Basic class
# ============================================================

class Temperature:
    def __init__(self, celsius: float) -> None:
        if celsius < -273.15:
            raise ValueError(f"Temperature {celsius}°C is below absolute zero.")
        self._celsius = celsius

    @property
    def celsius(self) -> float:
        return self._celsius

    @property
    def fahrenheit(self) -> float:
        return self._celsius * 9 / 5 + 32

    @property
    def kelvin(self) -> float:
        return self._celsius + 273.15

    @classmethod
    def from_fahrenheit(cls, f: float) -> "Temperature":
        return cls((f - 32) * 5 / 9)

    def __str__(self) -> str:
        return f"{self._celsius}°C"

    def __repr__(self) -> str:
        return f"Temperature(celsius={self._celsius})"


t = Temperature(23.0)
print(t)                            # 23.0°C
print(repr(t))                      # Temperature(celsius=23.0)
print(t.fahrenheit)                 # 73.4
print(t.kelvin)                     # 296.15
print(Temperature.from_fahrenheit(212))

try:
    Temperature(-300)
except ValueError as e:
    print(e)


# ============================================================
# Exercise 2 — Instance vs class attributes
# ============================================================

class APIClient:
    MAX_RETRIES: int = 3
    _instance_count: int = 0

    def __init__(self, base_url: str, api_key: str) -> None:
        self.base_url = base_url
        self.api_key = api_key
        APIClient._instance_count += 1

    @classmethod
    def total_clients(cls) -> int:
        return cls._instance_count

    @staticmethod
    def is_valid_url(url: str) -> bool:
        return url.startswith("http://") or url.startswith("https://")

    def get(self, endpoint: str) -> str:
        return f"GET {self.base_url}/{endpoint} (key: {self.api_key[:4]}...)"


c1 = APIClient("https://api.openai.com", "sk-abc123")
c2 = APIClient("https://api.anthropic.com", "ant-xyz789")
c3 = APIClient("https://api.google.com", "goog-000111")

print(APIClient.total_clients())                    # 3
print(APIClient.is_valid_url("https://example.com"))  # True
print(APIClient.is_valid_url("ftp://example.com"))    # False
print(c1.get("v1/chat/completions"))


# ============================================================
# Exercise 3 — Properties and encapsulation
# ============================================================

class BankAccount:
    def __init__(self, owner: str, initial_balance: float = 0) -> None:
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative.")
        self.owner = owner
        self._balance = initial_balance

    @property
    def balance(self) -> float:
        return self._balance

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than zero.")
        self._balance += amount

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than zero.")
        if amount > self._balance:
            raise ValueError(f"Insufficient funds: balance is €{self._balance:.2f}.")
        self._balance -= amount

    def transfer(self, amount: float, target: "BankAccount") -> None:
        self.withdraw(amount)       # raises if insufficient
        target.deposit(amount)

    def __str__(self) -> str:
        return f"BankAccount(owner={self.owner}, balance=€{self._balance:,.2f})"


acc1 = BankAccount("Javi", 1000)
acc2 = BankAccount("Ana", 500)
acc1.deposit(200)
acc1.withdraw(100)
acc1.transfer(300, acc2)
print(acc1)
print(acc2)

try:
    acc1.withdraw(10000)
except ValueError as e:
    print(e)


# ============================================================
# Exercise 4 — Inheritance and super()
# ============================================================

class Notification:
    def __init__(self, title: str, message: str, priority: str = "normal") -> None:
        self.title = title
        self.message = message
        self.priority = priority

    def send(self) -> None:
        print(f"Sending [{self.priority}] notification: {self.title}")

    def __str__(self) -> str:
        return f"Notification: {self.title} ({self.priority})"


class EmailNotification(Notification):
    def __init__(self, title: str, message: str, recipient: str,
                 priority: str = "normal") -> None:
        super().__init__(title, message, priority)
        self.recipient = recipient

    def send(self) -> None:
        super().send()
        print(f"Email to: {self.recipient} — {self.message}")


class SlackNotification(Notification):
    def __init__(self, title: str, message: str, channel: str,
                 priority: str = "normal") -> None:
        super().__init__(title, message, priority)
        self.channel = channel

    def send(self) -> None:
        super().send()
        print(f"Slack #{self.channel} — {self.message}")


notifications: list[Notification] = [
    Notification("System update", "Scheduled maintenance tonight."),
    EmailNotification("Welcome", "Thanks for signing up!", "user@example.com"),
    SlackNotification("Deploy done", "v2.3.1 is live.", "deployments", priority="high"),
]

for n in notifications:
    n.send()
    print()


# ============================================================
# Exercise 5 — Composition
# ============================================================

class Prompt:
    def __init__(self, template: str) -> None:
        self.template = template

    def render(self, **kwargs: str) -> str:
        return self.template.format(**kwargs)

    def __repr__(self) -> str:
        preview = self.template[:30]
        return f"Prompt(template={preview!r})"


class Model:
    def __init__(self, name: str, max_tokens: int = 1000) -> None:
        self.name = name
        self.max_tokens = max_tokens

    def generate(self, prompt: str) -> str:
        return f"[{self.name}] Response to: {prompt[:50]}..."

    def __repr__(self) -> str:
        return f"Model(name={self.name!r})"


class Chain:
    def __init__(self, prompt: Prompt, model: Model) -> None:
        self.prompt = prompt
        self.model = model

    def run(self, **kwargs: str) -> str:
        rendered = self.prompt.render(**kwargs)
        return self.model.generate(rendered)

    def __str__(self) -> str:
        return f"Chain(prompt={self.prompt!r}, model={self.model!r})"


p = Prompt("Summarise the following text in {language}: {text}")
m = Model("claude-sonnet-4-6")
chain = Chain(p, m)
print(chain)
print(chain.run(language="Spanish", text="Python is a great language for AI."))


# ============================================================
# Exercise 6 — Dunder methods
# ============================================================

class Vector:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"Vector({self.x}, {self.y})"

    def __repr__(self) -> str:
        return f"Vector(x={self.x}, y={self.y})"

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar: float) -> "Vector":
        return Vector(self.x * scalar, self.y * scalar)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Vector):
            return NotImplemented
        return self.x == other.x and self.y == other.y

    def __len__(self) -> int:
        return round(self.magnitude)

    def __abs__(self) -> float:
        return self.magnitude

    @property
    def magnitude(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)


v1 = Vector(3, 4)
v2 = Vector(1, 2)
print(v1 + v2)          # Vector(4, 6)
print(v1 - v2)          # Vector(2, 2)
print(v1 * 3)           # Vector(9, 12)
print(v1 == v2)         # False
print(len(v1))          # 5
print(abs(v1))          # 5.0


# ============================================================
# Exercise 7 — Context manager
# ============================================================

# Part A: class-based Timer
class Timer:
    def __enter__(self) -> "Timer":
        self._start = time.perf_counter()
        return self

    def __exit__(self, *args: object) -> None:
        self.elapsed = time.perf_counter() - self._start
        print(f"Elapsed: {self.elapsed:.4f}s")


with Timer() as t:
    total = sum(range(1_000_000))
print(f"t.elapsed = {t.elapsed:.4f}s")


# Part B: contextmanager-based Timer
@contextmanager
def timer():
    start = time.perf_counter()
    yield
    elapsed = time.perf_counter() - start
    print(f"Elapsed: {elapsed:.4f}s")


with timer():
    total = sum(range(1_000_000))


# ============================================================
# Exercise 8 — Dataclasses
# ============================================================

@dataclass
class ModelConfig:
    name: str
    provider: str
    max_tokens: int = 4096
    temperature: float = 0.7
    tags: list[str] = field(default_factory=list)


@dataclass(frozen=True)
class ExperimentResult:
    model_name: str
    prompt: str
    response: str
    latency_ms: float
    tokens_used: int


gpt = ModelConfig("gpt-4o", "openai", max_tokens=128000)
claude = ModelConfig("claude-sonnet-4-6", "anthropic", max_tokens=200000, temperature=1.0)
gemini = ModelConfig("gemini-1.5-pro", "google", max_tokens=1_000_000, temperature=0.4)

gpt.tags.append("chat")
gpt.tags.append("vision")
claude.tags.append("chat")

experiments = [
    ExperimentResult("gpt-4o", "Explain RAG", "...", latency_ms=320.5, tokens_used=450),
    ExperimentResult("claude-sonnet-4-6", "Explain RAG", "...", latency_ms=180.2, tokens_used=380),
    ExperimentResult("gemini-1.5-pro", "Explain RAG", "...", latency_ms=540.1, tokens_used=510),
]

# Try to modify a frozen dataclass
try:
    experiments[0].latency_ms = 100  # type: ignore[misc]
except Exception as e:
    print(f"Cannot modify frozen dataclass: {e}")

# Sort by latency_ms
by_latency = sorted(experiments, key=lambda e: e.latency_ms)
for exp in by_latency:
    print(f"{exp.model_name}: {exp.latency_ms}ms — {exp.tokens_used} tokens")
