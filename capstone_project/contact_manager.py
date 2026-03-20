"""
Contact Manager — Capstone Project
Python Fundamentals · AI Engineering Roadmap

A command-line contact manager that persists data to a JSON file.
Run with: python contact_manager.py
"""

import json
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any


# ---------------------------------------------------------------------------
# Model
# ---------------------------------------------------------------------------

@dataclass
class Contact:
    id: int
    name: str
    email: str
    phone: str
    tags: list[str] = field(default_factory=list)


# ---------------------------------------------------------------------------
# Exceptions
# ---------------------------------------------------------------------------

class ContactNotFoundError(Exception):
    """Raised when a contact with the requested id does not exist."""


# ---------------------------------------------------------------------------
# Manager
# ---------------------------------------------------------------------------

class ContactManager:
    """Manages a collection of contacts with file-based persistence.

    All contacts are kept in memory as a list; they are loaded from a JSON
    file on initialisation and saved back after every write operation.
    """

    def __init__(self, filepath: Path) -> None:
        self._filepath: Path = filepath
        self._contacts: list[Contact] = self.load()

    # --- persistence --------------------------------------------------------

    def load(self) -> list[Contact]:
        """Load contacts from the JSON file.

        Returns an empty list and creates the file if it does not exist.
        """
        try:
            with open(self._filepath, "r", encoding="utf-8") as fh:
                data: list[dict[str, Any]] = json.load(fh)
            return [
                Contact(
                    id=item["id"],
                    name=item["name"],
                    email=item["email"],
                    phone=item["phone"],
                    tags=item.get("tags", []),
                )
                for item in data
            ]
        except FileNotFoundError:
            self._filepath.parent.mkdir(parents=True, exist_ok=True)
            return []
        except (json.JSONDecodeError, KeyError):
            print("Warning: contacts file is corrupted. Starting with empty list.")
            return []

    def save(self, contacts: list[Contact]) -> None:
        """Persist contacts to the JSON file.

        Args:
            contacts: The list of contacts to write.
        """
        try:
            self._filepath.parent.mkdir(parents=True, exist_ok=True)
            with open(self._filepath, "w", encoding="utf-8") as fh:
                json.dump([asdict(c) for c in contacts], fh, indent=2, ensure_ascii=False)
        except OSError as exc:
            print(f"Error saving contacts: {exc}")

    def _persist(self) -> None:
        """Save the current in-memory list to disk."""
        self.save(self._contacts)

    def _next_id(self) -> int:
        """Return the next available id (never reuses a deleted id)."""
        if not self._contacts:
            return 1
        return max(c.id for c in self._contacts) + 1

    # --- queries ------------------------------------------------------------

    def get_all(self) -> list[Contact]:
        """Return all contacts."""
        return list(self._contacts)

    def get_by_id(self, contact_id: int) -> Contact | None:
        """Return the contact with the given id, or None if not found.

        Args:
            contact_id: The id to look up.
        """
        for contact in self._contacts:
            if contact.id == contact_id:
                return contact
        return None

    def search(self, query: str) -> list[Contact]:
        """Return contacts whose name or email matches the query.

        The match is case-insensitive and partial.

        Args:
            query: The search string.
        """
        q = query.lower()
        return [
            c for c in self._contacts
            if q in c.name.lower() or q in c.email.lower()
        ]

    def filter_by_tag(self, tag: str) -> list[Contact]:
        """Return contacts that have the given tag (case-insensitive).

        Args:
            tag: The tag to filter by.
        """
        t = tag.lower()
        return [c for c in self._contacts if t in [tg.lower() for tg in c.tags]]

    # --- mutations ----------------------------------------------------------

    def add(self, name: str, email: str, phone: str, tags: list[str]) -> Contact:
        """Create and store a new contact.

        Args:
            name:  Full name.
            email: Email address.
            phone: Phone number.
            tags:  Optional list of tags.

        Returns:
            The newly created Contact.
        """
        contact = Contact(
            id=self._next_id(),
            name=name,
            email=email,
            phone=phone,
            tags=tags,
        )
        self._contacts.append(contact)
        self._persist()
        return contact

    def update(self, contact_id: int, **fields: Any) -> Contact | None:
        """Update one or more fields of an existing contact.

        Args:
            contact_id: The id of the contact to update.
            **fields:   Keyword arguments mapping field names to new values.

        Returns:
            The updated Contact, or None if not found.

        Raises:
            ContactNotFoundError: If no contact with contact_id exists.
        """
        contact = self.get_by_id(contact_id)
        if contact is None:
            raise ContactNotFoundError(f"No contact with id {contact_id}.")
        for key, value in fields.items():
            if hasattr(contact, key):
                setattr(contact, key, value)
        self._persist()
        return contact

    def delete(self, contact_id: int) -> bool:
        """Delete the contact with the given id.

        Args:
            contact_id: The id to delete.

        Returns:
            True if a contact was deleted, False if the id was not found.
        """
        original_len = len(self._contacts)
        self._contacts = [c for c in self._contacts if c.id != contact_id]
        if len(self._contacts) < original_len:
            self._persist()
            return True
        return False


# ---------------------------------------------------------------------------
# Display helpers
# ---------------------------------------------------------------------------

def display_contact(contact: Contact) -> None:
    """Print a single contact in a readable format.

    Args:
        contact: The contact to display.
    """
    tags_str = ", ".join(contact.tags) if contact.tags else "—"
    print(f"  ID    : {contact.id}")
    print(f"  Name  : {contact.name}")
    print(f"  Email : {contact.email}")
    print(f"  Phone : {contact.phone}")
    print(f"  Tags  : {tags_str}")


def display_table(contacts: list[Contact]) -> None:
    """Print a list of contacts as a formatted table.

    Args:
        contacts: The contacts to display.
    """
    if not contacts:
        print("  (no contacts to show)")
        return

    header = f"  {'ID':<5} {'Name':<22} {'Email':<28} {'Phone':<15} Tags"
    separator = "  " + "-" * (len(header) - 2)
    print(header)
    print(separator)
    for c in contacts:
        tags_str = ", ".join(c.tags) if c.tags else "—"
        print(f"  {c.id:<5} {c.name:<22} {c.email:<28} {c.phone:<15} {tags_str}")


# ---------------------------------------------------------------------------
# UI helpers
# ---------------------------------------------------------------------------

def _prompt(label: str, current: str = "") -> str:
    """Prompt the user for input, showing the current value if editing.

    Args:
        label:   The prompt label.
        current: The current value (shown in brackets when editing).

    Returns:
        The user's input, or current if they pressed Enter.
    """
    if current:
        value = input(f"  {label} [{current}]: ").strip()
        return value if value else current
    return input(f"  {label}: ").strip()


def _prompt_tags(current: list[str] | None = None) -> list[str]:
    """Prompt the user for comma-separated tags.

    Args:
        current: Existing tags shown as default when editing.

    Returns:
        A list of stripped tag strings (may be empty).
    """
    current_str = ", ".join(current) if current else ""
    raw = _prompt("Tags (comma-separated, optional)", current_str)
    if not raw:
        return []
    return [t.strip() for t in raw.split(",") if t.strip()]


# ---------------------------------------------------------------------------
# Feature handlers
# ---------------------------------------------------------------------------

def handle_add(manager: ContactManager) -> None:
    """Prompt for contact details and add a new contact."""
    print("\n--- Add contact ---")
    name = _prompt("Name")
    if not name:
        print("  Name cannot be empty. Cancelled.")
        return
    email = _prompt("Email")
    phone = _prompt("Phone")
    tags = _prompt_tags()
    contact = manager.add(name, email, phone, tags)
    print(f"\n  Contact #{contact.id} added successfully.")


def handle_list(manager: ContactManager) -> None:
    """Display all contacts in a table."""
    print("\n--- All contacts ---")
    display_table(manager.get_all())


def handle_search(manager: ContactManager) -> None:
    """Search contacts by name or email."""
    print("\n--- Search contacts ---")
    query = _prompt("Search (name or email)")
    if not query:
        print("  Search query cannot be empty.")
        return
    results = manager.search(query)
    if not results:
        print(f'  No contacts found matching "{query}".')
    else:
        print(f"\n  {len(results)} result(s):")
        display_table(results)


def handle_edit(manager: ContactManager) -> None:
    """Edit an existing contact by id."""
    print("\n--- Edit contact ---")
    try:
        contact_id = int(_prompt("Contact id"))
    except ValueError:
        print("  Invalid id.")
        return

    contact = manager.get_by_id(contact_id)
    if contact is None:
        print(f"  No contact with id {contact_id}.")
        return

    print("\n  Current values (press Enter to keep):")
    name = _prompt("Name", contact.name)
    email = _prompt("Email", contact.email)
    phone = _prompt("Phone", contact.phone)
    tags = _prompt_tags(contact.tags)

    try:
        manager.update(contact_id, name=name, email=email, phone=phone, tags=tags)
        print(f"\n  Contact #{contact_id} updated.")
    except ContactNotFoundError as exc:
        print(f"  Error: {exc}")


def handle_delete(manager: ContactManager) -> None:
    """Delete a contact by id after confirmation."""
    print("\n--- Delete contact ---")
    try:
        contact_id = int(_prompt("Contact id"))
    except ValueError:
        print("  Invalid id.")
        return

    contact = manager.get_by_id(contact_id)
    if contact is None:
        print(f"  No contact with id {contact_id}.")
        return

    print()
    display_contact(contact)
    confirm = input("\n  Delete this contact? (y/n): ").strip().lower()
    if confirm == "y":
        manager.delete(contact_id)
        print(f"  Contact #{contact_id} deleted.")
    else:
        print("  Cancelled.")


def handle_filter_by_tag(manager: ContactManager) -> None:
    """Show contacts that have a specific tag."""
    print("\n--- Filter by tag ---")
    tag = _prompt("Tag")
    if not tag:
        print("  Tag cannot be empty.")
        return
    results = manager.filter_by_tag(tag)
    if not results:
        print(f'  No contacts found with tag "{tag}".')
    else:
        print(f"\n  {len(results)} contact(s) tagged '{tag}':")
        display_table(results)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

MENU = """\
\n=== Contact Manager ===
1. Add contact
2. List all contacts
3. Search contacts
4. Edit contact
5. Delete contact
6. Filter by tag
0. Save and quit
"""

HANDLERS = {
    "1": handle_add,
    "2": handle_list,
    "3": handle_search,
    "4": handle_edit,
    "5": handle_delete,
    "6": handle_filter_by_tag,
}


def main() -> None:
    """Run the interactive contact manager menu loop."""
    data_path = Path(__file__).parent / "data" / "contacts.json"
    manager = ContactManager(data_path)

    print("Contact Manager loaded.")
    total = len(manager.get_all())
    print(f"{total} contact(s) in database.")

    while True:
        print(MENU)
        choice = input("Choose an option: ").strip()

        if choice == "0":
            manager.save(manager.get_all())
            print("Contacts saved. Goodbye!")
            break
        elif choice in HANDLERS:
            HANDLERS[choice](manager)
        else:
            print("  Invalid option. Please choose a number from the menu.")


if __name__ == "__main__":
    main()
