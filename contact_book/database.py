from typing import List
import datetime
from contact_book.model import Contact
from contact_book import db, ContactQuery


def create(contact: Contact) -> None:
    contact.position = len(db) + 1
    new_contact = {
        'name': contact.name,
        'contact_number': contact.contact_number,
        'position': contact.position,
        'date_created': contact.date_created,
        'date_updated': contact.date_updated
    }
    db.insert(new_contact)


def read() -> List[Contact]:
    results = db.all()
    contacts = []
    for result in results:
        new_contact = Contact(result['name'], result['contact_number'], result['position'],
                              result['date_created'], result['date_updated'])
        contacts.append(new_contact)
    return contacts


def update(position: int, name: str, contact_number: str) -> None:
    if name is not None and contact_number is not None:
        db.update({'name': name, 'contact_number': contact_number},
                  ContactQuery.position == position)
    elif name is not None:
        db.update({'name': name}, ContactQuery.position == position)
    elif contact_number is not None:
        db.update({'contact_number': contact_number},
                  ContactQuery.position == position)


def delete(position: int) -> None:
    count = len(db)
    db.remove(ContactQuery.position == position)
    for pos in range(position + 1, count):
        change_position(pos, pos - 1)


def change_position(old_position: int, new_position: int) -> None:
    db.update({'position': new_position},
              ContactQuery.position == old_position)


def remove_contact(position: int) -> None:
    print(f"Removing contact at position {position}...")
    delete(position)
    print("Contact removed successfully.")
    print("Updated contact book:")
    contacts = read()
    for contact in contacts:
        print(f"Name: {contact.name}, Contact Number: {contact.contact_number}, Position: {contact.position}")
        

# Test the modified code
if __name__ == "__main__":
    # Create some sample contacts
    contact1 = Contact("John Doe", "1234567890", 1, datetime.datetime.now(), datetime.datetime.now())
    contact2 = Contact("Jane Smith", "9876543210", 2, datetime.datetime.now(), datetime.datetime.now())
    contact3 = Contact("Bob Johnson", "5555555555", 3, datetime.datetime.now(), datetime.datetime.now())

    # Add contacts to the contact book
    create(contact1)
    create(contact2)
    create(contact3)

    # Display the initial contact book
    print("Initial contact book:")
    contacts = read()
    for contact in contacts:
        print(f"Name: {contact.name}, Contact Number: {contact.contact_number}, Position: {contact.position}")

    # Remove contact at position 2
    remove_contact(2)