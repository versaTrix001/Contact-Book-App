import re

class Contact:
    def __init__(self, name, email, phone, address, tags):
        self.name = name
        self.email = self.validate_email(email)
        self.phone = self.validate_phone(phone)
        self.address = address
        self.tags = tags

        
    @staticmethod
    def validate_email(email):
        while True:
            if re.match(r"[^@]+@[^@]+\.[^@]+", email):
                return email
            else:
                email = input("Enter valid email: ")

    @staticmethod
    def validate_phone(phone):
        while True:
            if re.match(r"^[0-9]{10}$", phone):
                return phone
            else:
                phone = input("Enter a valid phone number (10 digits): ")
   
    def to_dict(self):
        return {
            'name': self.name,
            'email': self.email,
            'phone': self.phone,
            'address': self.address,
            'tags': self.tags
        }

    def __str__(self):
        return f'Name: {self.name}, Email: {self.email}, Phone: {self.phone}, Address: {self.address}, Tags: {self.tags}'

    @classmethod
    def from_dict(cls, data):
        return cls(data['name'], data['email'], data['phone'], data['address'], data['tags'])