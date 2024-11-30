import sqlite3

# Способ 3: Телефонная книга с использованием SQLite

# Создайте и подключитесь к базе данных
conn = sqlite3.connect('phone_book.db')
cursor = conn.cursor()

# Создаем таблицу
cursor.execute('''
CREATE TABLE IF NOT EXISTS contacts (
    name TEXT PRIMARY KEY,
    phone TEXT NOT NULL
)
''')

def add_contact(name, phone):
    try:
        cursor.execute('INSERT INTO contacts (name, phone) VALUES (?, ?)', (name, phone))
        conn.commit()
        print(f"Контакт {name} добавлен.")
    except sqlite3.IntegrityError:
        print("Контакт с таким именем уже существует.")

def find_contact(name):
    cursor.execute('SELECT phone FROM contacts WHERE name = ?', (name,))
    contact = cursor.fetchone()
    return contact[0] if contact else "Контакт не найден."

def display_contacts():
    cursor.execute('SELECT * FROM contacts')
    for name, phone in cursor.fetchall():
        print(f"{name}: {phone}")

# Примеры использования
add_contact("Alice", "123-456-7890")
add_contact("Bob", "987-654-3210")

print(find_contact("Alice"))
display_contacts()

# Закрыть соединение с базой данных
conn.close()