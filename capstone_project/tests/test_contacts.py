"""
Tests for ContactManager — Capstone Project
Run with: python tests/test_contacts.py

Uses plain assert statements — no pytest or external libraries required.
All tests use an in-memory ContactManager (no real contacts.json is touched).
"""

import sys
from pathlib import Path

# Make sure the capstone_project package root is on the path so we can import
# contact_manager regardless of where this script is called from.
sys.path.insert(0, str(Path(__file__).parent.parent))

from contact_manager import Contact, ContactManager  # noqa: E402


def make_manager() -> ContactManager:
    """Return a fresh, empty ContactManager for each test.

    Uses a temporary file that is deleted before each call so that tests
    are fully isolated and do not affect the real data/contacts.json.
    """
    tmp = Path("/tmp/_test_contacts_tmp.json")
    if tmp.exists():
        tmp.unlink()
    return ContactManager(tmp)


# ---------------------------------------------------------------------------
# Test 1: Adding a contact returns a Contact with the correct name
# ---------------------------------------------------------------------------

def test_add_returns_correct_name() -> None:
    manager = make_manager()
    contact = manager.add("Alice Smith", "alice@example.com", "555-0001", [])
    assert contact.name == "Alice Smith", (
        f"Expected name 'Alice Smith', got '{contact.name}'"
    )


# ---------------------------------------------------------------------------
# Test 2: Adding two contacts gives them different ids
# ---------------------------------------------------------------------------

def test_two_contacts_have_different_ids() -> None:
    manager = make_manager()
    c1 = manager.add("Alice Smith", "alice@example.com", "555-0001", [])
    c2 = manager.add("Bob Jones", "bob@example.com", "555-0002", [])
    assert c1.id != c2.id, (
        f"Expected different ids, but both got id={c1.id}"
    )


# ---------------------------------------------------------------------------
# Test 3: Search finds a contact by partial name match
# ---------------------------------------------------------------------------

def test_search_finds_partial_name_match() -> None:
    manager = make_manager()
    manager.add("Alice Smith", "alice@example.com", "555-0001", [])
    manager.add("Bob Jones", "bob@example.com", "555-0002", [])
    results = manager.search("alice")
    assert len(results) == 1, f"Expected 1 result, got {len(results)}"
    assert results[0].name == "Alice Smith"


# ---------------------------------------------------------------------------
# Test 4: Search returns empty list when there is no match
# ---------------------------------------------------------------------------

def test_search_returns_empty_list_when_no_match() -> None:
    manager = make_manager()
    manager.add("Alice Smith", "alice@example.com", "555-0001", [])
    results = manager.search("zzznomatch")
    assert results == [], f"Expected empty list, got {results}"


# ---------------------------------------------------------------------------
# Test 5: Delete returns True for an existing contact
# ---------------------------------------------------------------------------

def test_delete_returns_true_for_existing_contact() -> None:
    manager = make_manager()
    contact = manager.add("Alice Smith", "alice@example.com", "555-0001", [])
    result = manager.delete(contact.id)
    assert result is True, f"Expected True, got {result}"
    assert manager.get_by_id(contact.id) is None, "Contact should be gone after deletion"


# ---------------------------------------------------------------------------
# Test 6: get_by_id returns None for a non-existent id
# ---------------------------------------------------------------------------

def test_get_by_id_returns_none_for_nonexistent_id() -> None:
    manager = make_manager()
    result = manager.get_by_id(9999)
    assert result is None, f"Expected None, got {result}"


# ---------------------------------------------------------------------------
# Runner
# ---------------------------------------------------------------------------

TESTS = [
    test_add_returns_correct_name,
    test_two_contacts_have_different_ids,
    test_search_finds_partial_name_match,
    test_search_returns_empty_list_when_no_match,
    test_delete_returns_true_for_existing_contact,
    test_get_by_id_returns_none_for_nonexistent_id,
]

if __name__ == "__main__":
    failed = 0
    for test in TESTS:
        try:
            test()
            print(f"  PASS  {test.__name__}")
        except AssertionError as exc:
            print(f"  FAIL  {test.__name__}: {exc}")
            failed += 1
        except Exception as exc:
            print(f"  ERROR {test.__name__}: {exc}")
            failed += 1

    print()
    if failed == 0:
        print("All tests passed")
    else:
        print(f"{failed} test(s) failed")
        sys.exit(1)
