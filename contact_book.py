
import json
from contact import Contact
from fuzzywuzzy import fuzz

class ContactBook:
    def __init__(self, filename):
        self.filename = filename
        self.contacts = self.load_contacts()

    def load_contacts(self):
        try:
            with open(self.filename, 'r') as file:
                data = json.load(file)
                return [Contact(**contact) for contact in data]
        except FileNotFoundError:
            return []

    def save_contacts(self):
        with open(self.filename, 'w') as file:
            json.dump([contact.to_dict() for contact in self.contacts], file)

    def add_contact(self, name, email, phone, address, tags):
        contact = Contact(name, email, phone, address, tags)
        self.contacts.append(contact)
        self.save_contacts()

    def search_contacts(self, name):
        return [contact for contact in self.contacts if fuzz.ratio(contact.name, name) > 50 or any(fuzz.ratio(tag, name) > 50 for tag in contact.tags)]

    def update_contact(self, name, email=None, phone=None, address=None, tags=None):
        contact_updated = False
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                if email:
                    email = Contact.validate_email(email)
                    contact.email = email
                if phone:
                    phone = Contact.validate_phone(phone)
                    contact.phone = phone
                if address:
                    contact.address = address
                if tags:
                    contact.tags = tags
                self.save_contacts()
                contact_updated = True
                break
        if not contact_updated:
            print(f"No contact found with the name {name}.")

    def delete_contact(self, name):
        self.contacts = [contact for contact in self.contacts if contact.name != name]
        self.save_contacts()

    def list_contacts(self):
        return self.contacts