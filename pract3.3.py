phone_book = {}

def add_contact(name, phone):
    phone_book[name] = phone
    print(f"Контакт {name} добавлен.")

def find_contact(name):
    return phone_book.get(name, "Контакт не найден.")

def display_contacts():
    for name, phone in phone_book.items():
        print(f"{name}: {phone}")

# Примеры использования
add_contact("Alice", "123-456-7890")
add_contact("Bob", "987-654-3210")

print(find_contact("Alice"))
display_contacts()