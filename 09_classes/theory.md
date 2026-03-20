# 09 — Classes and Object-Oriented Programming

Object-oriented programming (OOP) is a paradigm that structures programs around **objects** — entities that combine data and behaviour. Instead of having separate data and functions, OOP groups them into cohesive units called classes.

Everything in Python is already an object. Strings, lists, dictionaries — they all have attributes and methods because they are instances of classes. This lesson shows you how to build your own.

---

## Core OOP concepts

**Encapsulation** — groups related data and behaviour inside a class, hiding internal details and exposing only what is necessary.

**Inheritance** — lets you create new classes based on existing ones, reusing and extending their functionality.

**Polymorphism** — allows different classes to implement the same method in different ways, sharing a common interface.

**Abstraction** — simplifies complex systems by focusing on essential aspects and hiding unnecessary details.

---

## Classes and objects

A **class** is a blueprint for creating objects. An **object** (or instance) is a concrete realisation of that blueprint.

```python
class Car:
    pass

# Create multiple independent objects from the same class
car1 = Car()
car2 = Car()

print(car1 is car2)  # False — different objects
```

> Class names use **PascalCase** by convention: `Car`, `BankAccount`, `DataLoader`.

---

## __init__, self and attributes

### __init__

`__init__` is the constructor — Python calls it automatically when you create a new object. Use it to initialise instance attributes:

```python
class Car:
    def __init__(self, model, horsepower, consumption):
        self.model = model
        self.horsepower = horsepower
        self.consumption = consumption
        self.mileage = 0  # default value

renault = Car("Clio", 90, 5.5)
bmw = Car("i3", 170, 0)

print(renault.model)     # "Clio"
print(bmw.horsepower)    # 170
```

### self

`self` is a reference to the current object. It must be the first parameter of every instance method. Python passes it automatically — you never include it when calling:

```python
class Dog:
    def bark(self):
        print("Woof!")

dog = Dog()
dog.bark()  # Python internally calls Dog.bark(dog)
```

### Instance attributes vs class attributes

**Instance attributes** are unique to each object — defined in `__init__` with `self`:

```python
class Car:
    def __init__(self, model):
        self.model = model  # unique per object
```

**Class attributes** are shared by all instances — defined directly in the class body:

```python
class Car:
    wheels = 4  # shared by all cars

    def __init__(self, model):
        self.model = model

renault = Car("Clio")
bmw = Car("i3")

print(renault.wheels)  # 4
print(bmw.wheels)      # 4

Car.wheels = 6         # modifying affects all instances
print(renault.wheels)  # 6
```

### Attribute access conventions

Python does not have truly private attributes. The underscore convention signals intent:

```python
class BankAccount:
    def __init__(self, balance):
        self.balance = balance        # public — access freely
        self._internal = 0           # protected — internal use, avoid from outside
        self.__private = "secret"    # name-mangled — harder to access accidentally
```

Use methods to control how attributes are read and modified:

```python
class BankAccount:
    def __init__(self):
        self._balance = 0

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount

    def get_balance(self):
        return self._balance
```

---

## Methods

### Instance methods

Standard methods — receive `self` and can access instance and class attributes:

```python
class Car:
    def __init__(self, model):
        self.model = model
        self._mileage = 0

    def drive(self, km):
        if km > 0:
            self._mileage += km

    def show_info(self):
        print(f"{self.model} — {self._mileage} km")
```

### Class methods

Operate on the class itself, not on instances. Receive `cls` as first parameter. Useful as factory methods (alternative constructors):

```python
class Person:
    count = 0

    def __init__(self, name):
        self.name = name
        Person.count += 1

    @classmethod
    def total(cls):
        return f"Total persons: {cls.count}"

    @classmethod
    def anonymous(cls):
        """Factory method — alternative constructor"""
        return cls("Anonymous")

p1 = Person("Ana")
p2 = Person("Juan")

print(Person.total())   # Total persons: 2

anon = Person.anonymous()
print(anon.name)        # Anonymous
```

### Static methods

Neither `self` nor `cls` — utility functions logically grouped inside a class:

```python
class MathUtils:
    @staticmethod
    def is_even(n):
        return n % 2 == 0

    @staticmethod
    def clamp(value, min_val, max_val):
        return max(min_val, min(max_val, value))

MathUtils.is_even(4)          # True
MathUtils.clamp(15, 0, 10)    # 10
```

**When to use each:**
- Instance method → needs `self` — accesses instance state.
- `@classmethod` → needs `cls` — operates on class state or creates instances.
- `@staticmethod` → needs neither — utility logic that belongs conceptually with the class.

---

## Properties

`@property` lets you access a method as if it were an attribute, while keeping control over reads and writes:

```python
class Car:
    def __init__(self, model):
        self.model = model
        self._mileage = 0

    @property
    def mileage(self):
        """Getter — called when you read car.mileage"""
        return self._mileage

    @mileage.setter
    def mileage(self, km):
        """Setter — called when you assign car.mileage = value"""
        if km >= self._mileage:
            self._mileage = km
        else:
            raise ValueError("Mileage cannot decrease")

car = Car("Clio")
car.mileage = 5000      # calls setter
print(car.mileage)      # calls getter → 5000
car.mileage = 3000      # ValueError: Mileage cannot decrease
```

You can also define a `@property` with no setter to make an attribute read-only:

```python
class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        import math
        return math.pi * self.radius ** 2

c = Circle(5)
print(c.area)   # 78.53...
c.area = 100    # AttributeError — no setter defined
```

---

## Inheritance

Inheritance lets a class (child) reuse and extend the behaviour of another class (parent).

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Some sound...")

class Dog(Animal):
    def speak(self):
        print("Woof!")

class Cat(Animal):
    def speak(self):
        print("Meow!")

animals = [Dog("Rex"), Cat("Whiskers"), Dog("Buddy")]
for animal in animals:
    animal.speak()
# Woof!
# Meow!
# Woof!
```

### super()

`super()` calls the parent class's method. Use it to extend rather than replace parent behaviour:

```python
class Animal:
    def __init__(self, name):
        self.name = name
        print(f"Animal created: {name}")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)   # call parent __init__
        self.breed = breed
        print(f"Dog breed: {breed}")

dog = Dog("Rex", "Labrador")
# Animal created: Rex
# Dog breed: Labrador
```

### Checking inheritance

```python
isinstance(dog, Dog)     # True
isinstance(dog, Animal)  # True — Dog inherits from Animal
issubclass(Dog, Animal)  # True
```

### Multiple inheritance

Python supports inheriting from multiple parents — use carefully:

```python
class Flyable:
    def fly(self):
        print("Flying...")

class Swimmable:
    def swim(self):
        print("Swimming...")

class Duck(Flyable, Swimmable):
    def quack(self):
        print("Quack!")

duck = Duck()
duck.fly()    # Flying...
duck.swim()   # Swimming...
duck.quack()  # Quack!

# Method Resolution Order — how Python resolves method lookups
print(Duck.__mro__)
# Duck → Flyable → Swimmable → object
```

---

## Composition vs inheritance

Inheritance models "is a" relationships. Composition models "has a" relationships — and is often the better choice:

```python
# Inheritance — "ElectricCar IS A Car"
class ElectricCar(Car):
    def __init__(self, model, battery_capacity):
        super().__init__(model, 0, 0)
        self.battery_capacity = battery_capacity

# Composition — "ElectricCar HAS A Battery"
class Battery:
    def __init__(self, capacity_kwh, weight_kg):
        self.capacity = capacity_kwh
        self.weight = weight_kg

    def show_specs(self):
        print(f"{self.capacity} kWh, {self.weight} kg")

class ElectricCar(Car):
    def __init__(self, model, battery):
        super().__init__(model, 0, 0)
        self.battery = battery   # has-a relationship

    def show_battery(self):
        self.battery.show_specs()

battery = Battery(75, 480)
tesla = ElectricCar("Model 3", battery)
tesla.show_battery()  # 75 kWh, 480 kg
```

**Rule of thumb**: prefer composition. Use inheritance only when there is a genuine "is a" relationship and you want to share behaviour, not just data.

---

## Dunder methods

Dunder (double underscore) methods, also called magic methods, let you customise how your objects behave with Python's built-in operations.

### __str__ and __repr__

```python
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        """Human-readable — used by print() and str()"""
        return f"{self.title} by {self.author}"

    def __repr__(self):
        """Developer-readable — used in the REPL and repr()"""
        return f"Book(title={self.title!r}, author={self.author!r}, pages={self.pages})"

book = Book("1984", "George Orwell", 328)
print(book)       # 1984 by George Orwell
repr(book)        # Book(title='1984', author='George Orwell', pages=328)
```

### __len__, __eq__, __lt__

```python
class Book:
    ...

    def __len__(self):
        return self.pages

    def __eq__(self, other):
        return self.title == other.title and self.author == other.author

    def __lt__(self, other):
        return self.pages < other.pages

b1 = Book("1984", "George Orwell", 328)
b2 = Book("Brave New World", "Huxley", 311)

len(b1)       # 328
b1 == b2      # False
b1 < b2       # False (328 > 311)
sorted([b1, b2])  # sorted by pages — uses __lt__
```

### __contains__ and __getitem__

```python
class Library:
    def __init__(self):
        self._books = []

    def add(self, book):
        self._books.append(book)

    def __contains__(self, title):
        return any(b.title == title for b in self._books)

    def __getitem__(self, index):
        return self._books[index]

    def __len__(self):
        return len(self._books)

lib = Library()
lib.add(Book("1984", "Orwell", 328))

"1984" in lib      # True — uses __contains__
lib[0]             # first book — uses __getitem__
len(lib)           # 1 — uses __len__
```

---

## Context managers

In lesson `07_errors_and_exceptions` we used `with open(...)` and promised to explain how to build your own. Here it is.

A context manager implements two dunder methods:
- `__enter__` — runs when entering the `with` block, returns the resource.
- `__exit__` — runs when leaving the block, even if an exception occurred.

```python
class DatabaseConnection:
    def __init__(self, host):
        self.host = host
        self.connection = None

    def __enter__(self):
        print(f"Connecting to {self.host}")
        self.connection = f"conn:{self.host}"  # simulate connection
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Closing connection")
        self.connection = None
        return False  # False = don't suppress exceptions

with DatabaseConnection("localhost") as conn:
    print(f"Using {conn}")
    # do work here

# Output:
# Connecting to localhost
# Using conn:localhost
# Closing connection
```

`__exit__` receives exception information if one occurred. Returning `True` suppresses the exception; `False` lets it propagate:

```python
def __exit__(self, exc_type, exc_val, exc_tb):
    self.connection = None
    if exc_type is ValueError:
        print(f"Caught ValueError: {exc_val}")
        return True  # suppress it
    return False  # let everything else propagate
```

### contextlib.contextmanager — the simpler way

For simple cases, use the `@contextmanager` decorator instead of a full class:

```python
from contextlib import contextmanager

@contextmanager
def timer():
    import time
    start = time.time()
    yield  # code inside the with block runs here
    elapsed = time.time() - start
    print(f"Elapsed: {elapsed:.4f}s")

with timer():
    sum(range(1_000_000))
# Elapsed: 0.0412s
```

---

## Dataclasses

For classes that are primarily data containers, `@dataclass` eliminates boilerplate — it auto-generates `__init__`, `__repr__` and `__eq__`:

```python
from dataclasses import dataclass, field

@dataclass
class Point:
    x: float
    y: float

p = Point(1.0, 2.0)
print(p)         # Point(x=1.0, y=2.0)
p == Point(1.0, 2.0)  # True

@dataclass
class User:
    name: str
    age: int
    tags: list = field(default_factory=list)  # mutable default — use field()
    active: bool = True

u = User("Javi", 29)
print(u)  # User(name='Javi', age=29, tags=[], active=True)
```

Use `frozen=True` for immutable dataclasses (similar to a named tuple):

```python
@dataclass(frozen=True)
class Coordinate:
    lat: float
    lon: float

coord = Coordinate(40.4, -3.7)
coord.lat = 0  # FrozenInstanceError
```

Dataclasses are very common in AI engineering for representing structured data — API request/response schemas, model configurations, pipeline parameters.

---

## Summary

**Core concepts:**
- **Class** — blueprint, defined with PascalCase.
- **Object** — instance of a class, created by calling the class.
- **`__init__`** — constructor, initialises instance attributes.
- **`self`** — reference to the current object, first parameter of instance methods.
- **Instance attributes** — unique per object, defined with `self`.
- **Class attributes** — shared by all instances, defined in class body.

**Methods:**
- Instance method — `self`, accesses instance state.
- `@classmethod` — `cls`, operates on class; useful as factory methods.
- `@staticmethod` — no `self` or `cls`, utility logic grouped in the class.
- `@property` — method accessed as an attribute; add a setter for controlled writes.

**Inheritance:**
- Child class inherits all attributes and methods from parent.
- `super()` — calls parent method; always use in `__init__` when extending.
- Prefer composition ("has a") over inheritance ("is a") when in doubt.

**Dunder methods:**
- `__str__` / `__repr__` — string representations.
- `__len__`, `__eq__`, `__lt__` — support built-in operations.
- `__enter__` / `__exit__` — context manager protocol.

**Context managers:**
- Implement `__enter__` and `__exit__` for resource management.
- Or use `@contextmanager` from `contextlib` for simple cases.

**Dataclasses:**
- Use `@dataclass` for data containers — auto-generates boilerplate.
- Use `field(default_factory=...)` for mutable defaults.
- Use `frozen=True` for immutable instances.

**Best practices:**
- One class, one responsibility.
- Keep `__init__` simple — no complex logic.
- Use `_name` convention for internal attributes.
- Always implement `__repr__` — it is invaluable for debugging.
- Prefer composition over inheritance.
- Use dataclasses for simple data containers.

In the next lesson we will cover modular programming — how to organise code across multiple files and packages.