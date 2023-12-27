import datetime


class Contact:
    def __init__(self, name, contact_number, position=None, date_created=None, date_updated=None, email=None, address=None, new_field=None, street_name=None):
        self.name = name
        self.contact_number = contact_number
        self.position = position
        self.date_created = date_created if date_created is not None else datetime.datetime.now().isoformat()
        self.date_updated = date_updated if date_updated is not None else datetime.datetime.now().isoformat()
        self.email = email
        self.address = address
        self.new_field = new_field
        self.street_name = street_name

    def __repr__(self) -> str:
        return f"({self.name}, {self.contact_number}, {self.position}, {self.date_created}, {self.date_updated}, {self.email}, {self.address}, {self.new_field}, {self.street_name})"