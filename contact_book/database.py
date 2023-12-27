from typing import List
import datetime
from contact_book.model import Contact
from contact_book import db, ContactQuery


def create(contact: Contact) -> None:
    contact.position = len(db) + 1
    new_contact = {
        'name': contact.name,
        'contact_number': contact.contact_number,
        'email': contact.email,
        'address': contact.address,
        'street_name': contact.street_name,  # Added the new field 'street_name'
        'position': contact.position,
        'date_created': contact.date_created,
        'date_updated': contact.date_updated
    }
    db.insert(new_contact)


def read() -> List[Contact]:
    results = db.all()
    contacts = []
    for result in results:
        new_contact = Contact(result['name'], result['contact_number'], result['email'], result['address'], result['street_name'],  # Added 'street_name'
                              result['position'], result['date_created'], result['date_updated'])
        contacts.append(new_contact)
    return contacts


def update(position: int, name: str, contact_number: str, email: str, address: str, street_name: str) -> None:
    if name is not None and contact_number is not None and email is not None and address is not None and street_name is not None:  # Added 'street_name'
        db.update({'name': name, 'contact_number': contact_number, 'email': email, 'address': address, 'street_name': street_name},
                  ContactQuery.position == position)
    elif name is not None and contact_number is not None and email is not None and address is not None:
        db.update({'name': name, 'contact_number': contact_number, 'email': email, 'address': address},
                  ContactQuery.position == position)
    elif name is not None and contact_number is not None and email is not None:
        db.update({'name': name, 'contact_number': contact_number, 'email': email},
                  ContactQuery.position == position)
    elif name is not None and contact_number is not None and address is not None:
        db.update({'name': name, 'contact_number': contact_number, 'address': address},
                  ContactQuery.position == position)
    elif name is not None and email is not None and address is not None:
        db.update({'name': name, 'email': email, 'address': address},
                  ContactQuery.position == position)
    elif contact_number is not None and email is not None and address is not None:
        db.update({'contact_number': contact_number, 'email': email, 'address': address},
                  ContactQuery.position == position)
    elif name is not None and contact_number is not None:
        db.update({'name': name, 'contact_number': contact_number},
                  ContactQuery.position == position)
    elif name is not None and email is not None:
        db.update({'name': name, 'email': email},
                  ContactQuery.position == position)
    elif name is not None and address is not None:
        db.update({'name': name, 'address': address},
                  ContactQuery.position == position)
    elif contact_number is not None and email is not None:
        db.update({'contact_number': contact_number, 'email': email},
                  ContactQuery.position == position)
    elif contact_number is not None and address is not None:
        db.update({'contact_number': contact_number, 'address': address},
                  ContactQuery.position == position)
    elif email is not None and address is not None:
        db.update({'email': email, 'address': address},
                  ContactQuery.position == position)
    elif name is not None:
        db.update({'name': name}, ContactQuery.position == position)
    elif contact_number is not None:
        db.update({'contact_number': contact_number},
                  ContactQuery.position == position)
    elif email is not None:
        db.update({'email': email}, ContactQuery.position == position)
    elif address is not None:
        db.update({'address': address}, ContactQuery.position == position)


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
        print(f"Name: {contact.name}, Contact Number: {contact.contact_number}, Email: {contact.email}, Address: {contact.address}, Street Name: {contact.street_name}, Position: {contact.position}")


# Test the modified code
if __name__ == "__main__":
    # Create some sample contacts
    contact1 = Contact("John Doe", "1234567890", "john.doe@example.com", "123 Main St", "Street 1", 1, datetime.datetime.now(), datetime.datetime.now())  # Added 'street_name'
    contact2 = Contact("Jane Smith", "9876543210", "jane.smith@example.com", "456 Elm St", "Street 2", 2, datetime.datetime.now(), datetime.datetime.now())  # Added 'street_name'
    contact3 = Contact("Bob Johnson", "5555555555", "bob.johnson@example.com", "789 Oak St", "Street 3", 3, datetime.datetime.now(), datetime.datetime.now())  # Added 'street_name'

    # Add contacts to the contact book
    create(contact1)
    create(contact2)
    create(contact3)

    # Display the initial contact book
    print("Initial contact book:")
    contacts = read()
    for contact in contacts:
        print(f"Name: {contact.name}, Contact Number: {contact.contact_number}, Email: {contact.email}, Address: {contact.address}, Street Name: {contact.street_name}, Position: {contact.position}")

    # Remove contact at position 2
    remove_contact(2)