
import unittest
from contact import Contact

class TestContact(unittest.TestCase):

    def setUp(self):
        self.contact = Contact('John Doe', 'john.doe@example.com', '1234567890', '123 Street, City, Country', ['friend'])

    def test_email(self):
        self.assertEqual(self.contact.email, 'john.doe@example.com')

    def test_tag(self):
        self.assertEqual(self.contact.tags, ['friend'])

    def test_invalid_email(self):
        email = input("Enter a valid email: ")
        self.assertTrue(Contact.validate_email(email))

    def test_phone_number(self):
        self.assertEqual(self.contact.phone, '1234567890')

    def test_invalid_phone_number(self):
        phone = input("Enter a valid phone number (10 digits): ")
        self.assertTrue(Contact.validate_phone(phone))

    def test_address(self):
        self.assertEqual(self.contact.address, '123 Street, City, Country')

    def test_name(self):
        self.assertEqual(self.contact.name, 'John Doe')

if __name__ == '__main__':
    unittest.main()
