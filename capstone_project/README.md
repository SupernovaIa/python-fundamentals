# Capstone Project — Contact Manager

A command-line contact manager built with Python's standard library.
This is the final project of the **Python Fundamentals** module in the AI Engineering Roadmap.

---

## How to run

```bash
# From the repo root or from inside capstone_project/
python contact_manager.py
```

No external dependencies — pure stdlib only.

## How to run the tests

```bash
python tests/test_contacts.py
```

Expected output:

```
  PASS  test_add_returns_correct_name
  PASS  test_two_contacts_have_different_ids
  PASS  test_search_finds_partial_name_match
  PASS  test_search_returns_empty_list_when_no_match
  PASS  test_delete_returns_true_for_existing_contact
  PASS  test_get_by_id_returns_none_for_nonexistent_id

All tests passed
```

---

## Files

| File | Description |
|------|-------------|
| `contact_manager.py` | Main application — model, business logic, and interactive menu |
| `data/contacts.json` | Persisted contacts (created automatically on first run) |
| `tests/test_contacts.py` | 6 unit tests using plain `assert` statements |
| `theory.md` | Project spec and implementation guide |

---

## Features

- **Add** a contact with name, email, phone, and optional tags
- **List** all contacts in a formatted table
- **Search** by name or email (case-insensitive, partial match)
- **Edit** any field of an existing contact
- **Delete** a contact with confirmation prompt
- **Filter** contacts by tag
- Data **persists** between sessions via `data/contacts.json`

---

## Concepts covered

`dataclass` · `pathlib.Path` · `json` · type hints · custom exceptions ·
`try/except` · context managers · OOP · separation of concerns
