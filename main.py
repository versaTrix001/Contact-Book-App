##   Program execution starts from here  ##

from contact_book import ContactBook
import os

def main():
    contact_book = ContactBook(f"{os.path.dirname(os.path.abspath(__file__))}/../data/contacts.json")
    while True:
        print("1. Add a Contact")
        print("2. Search for a Contact")
        print("3. Update a Contact")
        print("4. Delete a Contact")
        print("5. List All Contacts")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            email = input("Enter email: ")
            phone = input("Enter phone number: ")
            address = input("Enter address: ")
            tags = input("Enter tags (comma separated): ").split(',')
            contact_book.add_contact(name, email, phone, address, tags)

        elif choice == '2':
            name = input("Enter name to search: ")
            contacts = contact_book.search_contacts(name)
            for contact in contacts:
                print(contact)

        elif choice == '3':
            name = input("Enter name of contact to update: ")
            email = input("Enter new email: ")
            phone = input("Enter new phone number: ")
            address = input("Enter new address: ")
            tags = input("Enter new tags (comma separated): ").split(',')
            contact_book.update_contact(name, email, phone, address, tags)

        elif choice == '4':
            name = input("Enter name of contact to delete: ")
            contact_book.delete_contact(name)

        elif choice == '5':
            contacts = contact_book.list_contacts()
            for contact in contacts:
                print(contact)

        elif choice == '6':
            break

        else:
            print("Invalid choice. Please choose a valid option.")


if __name__ == "__main__":
    main()
