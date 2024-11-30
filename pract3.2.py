class PhoneBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone):
        self.contacts[name] = phone
        print(f"Контакт {name} добавлен.")

    def find_contact(self, name):
        return self.contacts.get(name, "Контакт не найден.")

    def display_contacts(self):
        for name, phone in self.contacts.items():
            print(f"{name}: {phone}")

# Примеры использования
my_phone_book = PhoneBook()
my_phone_book.add_contact("Alice", "123-456-7890")
my_phone_book.add_contact("Bob", "987-654-3210")

print(my_phone_book.find_contact("Alice"))
my_phone_book.display_contacts()