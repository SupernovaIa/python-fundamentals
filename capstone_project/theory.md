# Capstone Project — Contact Manager

## What is this?

This is the final project of the Python Fundamentals module. You will build a command-line contact manager that runs in the terminal and persists data to a JSON file.

The goal is to apply everything you have learned in one coherent program:

| Lesson | Applied in |
|--------|-----------|
| Variables & types | Contact fields, id counter |
| Data structures | `list[Contact]`, `dict` for JSON serialisation |
| Control flow | Menu loop, search filtering |
| Functions | Helpers: `display_contact`, `display_table`, `main` |
| OOP | `Contact` dataclass, `ContactManager` class |
| File handling | Load/save JSON with `pathlib.Path` and context managers |
| Type hints | Full annotations on every function and class |
| Error handling | `ContactNotFoundError`, graceful FileNotFoundError, input validation |
| Modular thinking | Clear separation: model → manager → UI |

---

## Project structure

```
capstone_project/
├── README.md             ← how to run the project
├── contact_manager.py    ← main application (the file you write)
├── data/
│   └── contacts.json     ← created automatically on first run
└── tests/
    └── test_contacts.py  ← 6 basic tests, run with plain python
```

---

## The Contact model

A `Contact` is a `@dataclass` with these fields:

```python
@dataclass
class Contact:
    id: int           # auto-assigned, never reused
    name: str
    email: str
    phone: str
    tags: list[str]   # e.g. ["work", "friend"] — default empty list
```

---

## Features to implement

### 1 — Add contact
Prompt the user for name, email, phone, and optional comma-separated tags.
Assign a unique auto-incrementing id. Save immediately.

### 2 — List all contacts
Display all contacts in a clean table. Show a friendly message if the list is empty.

### 3 — Search contacts
Accept a query string. Return any contact whose `name` or `email` contains the
query (case-insensitive, partial match).

### 4 — Edit contact
Ask the user for an id, then for each field let them press Enter to keep the
current value or type a new one. Save immediately.

### 5 — Delete contact
Ask for an id, show the contact, ask for confirmation (`y/n`), then delete. Save.

### 6 — Filter by tag
Ask for a tag name. Show only contacts that have that tag.

### 0 — Save and quit
Save and exit the loop.

---

## Menu

```
=== Contact Manager ===
1. Add contact
2. List all contacts
3. Search contacts
4. Edit contact
5. Delete contact
6. Filter by tag
0. Save and quit

Choose an option:
```

---

## Technical requirements

### Classes and functions

| Name | Type | Responsibility |
|------|------|----------------|
| `Contact` | dataclass | Data model |
| `ContactNotFoundError` | exception | Raised when an id does not exist |
| `ContactManager` | class | All business logic and file I/O |
| `display_contact(contact)` | function | Print a single contact |
| `display_table(contacts)` | function | Print a formatted table |
| `main()` | function | Interactive menu loop |

### `ContactManager` methods

```python
def load(self) -> list[Contact]: ...
def save(self, contacts: list[Contact]) -> None: ...
def add(self, name: str, email: str, phone: str, tags: list[str]) -> Contact: ...
def get_all(self) -> list[Contact]: ...
def search(self, query: str) -> list[Contact]: ...
def get_by_id(self, contact_id: int) -> Contact | None: ...
def update(self, contact_id: int, **fields) -> Contact | None: ...
def delete(self, contact_id: int) -> bool: ...
def filter_by_tag(self, tag: str) -> list[Contact]: ...
```

### File handling rules
- Use `pathlib.Path` for all paths
- Use `with` for every file open
- Create `data/` automatically if it does not exist
- Load on startup, save on quit and after every write operation

### Error handling rules
- Never use bare `except:` — always name the exception
- Wrap all file operations in `try/except`
- Catch bad menu input (non-integer) without crashing
- Show a friendly message for empty search results

### Type hints
- Annotate every function parameter and return type
- Use `list[str]`, `dict[str, Any]` — import `Any` from `typing`

---

## Tests

Write 6 tests in `tests/test_contacts.py` using plain `assert` statements.
No pytest, no external libraries. Run with:

```bash
python tests/test_contacts.py
```

The tests must pass without touching `data/contacts.json` — use an in-memory
manager (pass a non-existent or temporary path).

Tests to write:

1. Adding a contact returns a `Contact` with the correct name
2. Adding two contacts gives them different ids
3. Search finds a contact by partial name match
4. Search returns an empty list when there is no match
5. Delete returns `True` for an existing contact
6. `get_by_id` returns `None` for a non-existent id

---

## Acceptance criteria

```bash
python contact_manager.py       # interactive menu works end-to-end
python tests/test_contacts.py   # prints "All tests passed"
```

Data must survive a restart: add a contact, quit, run again, and it is still there.

---

## Tips

- Start with the `Contact` dataclass and `ContactManager.load` / `ContactManager.save`.
  Get persistence working before building the menu.
- Keep `main()` thin: it reads input and calls manager methods, nothing else.
- The `update` method can use `setattr(contact, field, value)` to update fields
  dynamically from `**fields`.
- For the table, you can pad strings with f-string alignment: `f"{value:<20}"`.
