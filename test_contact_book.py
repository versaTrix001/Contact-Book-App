

import unittest
import tempfile
from contact_book import ContactBook
from contact import Contact

class TestContactBook(unittest.TestCase):

    def setUp(self):
        self.temp_file = tempfile.NamedTemporaryFile(delete=False, mode='w+')
        self.temp_file.write('[]')
        self.temp_file.seek(0)
        self.contact_book = ContactBook(self.temp_file.name)
        self.contact = Contact('John Doe', 'john.doe@example.com', '1234567890', '123 Street', ['friend'])

    def test_add_contact(self):
        self.contact_book.add_contact(self.contact.name, self.contact.email, self.contact.phone, self.contact.address, self.contact.tags)
        self.assertEqual(len(self.contact_book.contacts), 1)

    def test_search_contact(self):
        self.contact_book.add_contact(self.contact.name, self.contact.email, self.contact.phone, self.contact.address, self.contact.tags)
        result = self.contact_book.search_contacts('John Doe')
        self.assertEqual(result[0].name, self.contact.name)

    def test_update_contact(self):
        self.contact_book.add_contact(self.contact.name, self.contact.email, self.contact.phone, self.contact.address, self.contact.tags)
        self.contact_book.update_contact('John Doe', email='new.email@example.com')
        self.assertEqual(self.contact_book.contacts[0].email, 'new.email@example.com')

    def test_delete_contact(self):
        self.contact_book.add_contact(self.contact.name, self.contact.email, self.contact.phone, self.contact.address, self.contact.tags)
        self.contact_book.delete_contact('John Doe')
        self.assertEqual(len(self.contact_book.contacts), 0)

    def test_list_contacts(self):
        self.contact_book.add_contact(self.contact.name, self.contact.email, self.contact.phone, self.contact.address, self.contact.tags)
        contacts = self.contact_book.list_contacts()
        self.assertEqual(len(contacts), 1)

    def test_save_and_load_contacts(self):
        self.contact_book.add_contact(self.contact.name, self.contact.email, self.contact.phone, self.contact.address, self.contact.tags)
        self.contact_book.save_contacts()
        new_contact_book = ContactBook(self.temp_file.name)
        new_contact_book.load_contacts()
        self.assertEqual(len(new_contact_book.contacts), 1)

if __name__ == '__main__':
    unittest.main()