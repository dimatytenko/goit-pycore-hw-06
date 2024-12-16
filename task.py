# Технiчний опис завдання

# Розробіть систему для управління адресною книгою.

# Сутності:

# Field: Базовий клас для полів запису.
# Name: Клас для зберігання імені контакту. Обов'язкове поле.
# Phone: Клас для зберігання номера телефону. Має валідацію формату (10 цифр).
# Record: Клас для зберігання інформації про контакт, включаючи ім'я та список телефонів.
# AddressBook: Клас для зберігання та управління записами.

# Функціональність:

# AddressBook:Додавання записів.
# Пошук записів за іменем.
# Видалення записів за іменем.
# Record:Додавання телефонів.
# Видалення телефонів.
# Редагування телефонів.
# Пошук телефону.


# Рекомендації для виконання

# В якості старту ви можете взяти наступний базовий код для реалізації цього домашнього завдання:

# from collections import UserDict

# class Field:
#     def __init__(self, value):
#         self.value = value

#     def __str__(self):
#         return str(self.value)

# class Name(Field):
#     # реалізація класу
# 		pass

# class Phone(Field):
#     # реалізація класу
# 		pass

# class Record:
#     def __init__(self, name):
#         self.name = Name(name)
#         self.phones = []

#     # реалізація класу

#     def __str__(self):
#         return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

# class AddressBook(UserDict):
#     # реалізація класу
# 		pass


# Після реалізації ваш код має виконуватися наступним чином:

# # Створення нової адресної книги
#     book = AddressBook()

#     # Створення запису для John
#     john_record = Record("John")
#     john_record.add_phone("1234567890")
#     john_record.add_phone("5555555555")

#     # Додавання запису John до адресної книги
#     book.add_record(john_record)

#     # Створення та додавання нового запису для Jane
#     jane_record = Record("Jane")
#     jane_record.add_phone("9876543210")
#     book.add_record(jane_record)

#     # Виведення всіх записів у книзі
#     for name, record in book.data.items():
#         print(record)

#     # Знаходження та редагування телефону для John
#     john = book.find("John")
#     john.edit_phone("1234567890", "1112223333")

#     print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

#     # Пошук конкретного телефону у записі John
#     found_phone = john.find_phone("5555555555")
#     print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

#     # Видалення запису Jane
#     book.delete("Jane")

from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, value):
        if not value:
            raise ValueError("Name is required.")
        super().__init__(value)

class Phone(Field):
    def __init__(self, value):
        self.validate(value)
        super().__init__(value)

    @staticmethod
    def validate(value):
        if not value.isdigit() or len(value) != 10:
            raise ValueError("Invalid phone number. It must contain exactly 10 digits.")

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def delete_phone(self, phone):
        phone_to_remove = None
        for p in self.phones:
            if p.value == phone:
                phone_to_remove = p
                break
        if phone_to_remove:
            self.phones.remove(phone_to_remove)
        else:
            raise ValueError("Phone not found.")

    def edit_phone(self, old_phone, new_phone):
        for p in self.phones:
            if p.value == old_phone:
                Phone.validate(new_phone)
                p.value = new_phone
                return
        raise ValueError("Phone not found.")

    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p
        return None

    def __str__(self):
        phones = '; '.join(p.value for p in self.phones)
        return f"Contact name: {self.name.value}, phones: {phones}"

class AddressBook(UserDict):
    def add_record(self, record):
        if record.name.value in self.data:
            raise ValueError("Record with this name already exists.")
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name, None)

    def delete(self, name):
        if name in self.data:
            del self.data[name]
        else:
            raise ValueError("Record not found.")

# Example usage
if __name__ == "__main__":
    # Create a new address book
    book = AddressBook()

    # Create a record for John
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")

    # Add John's record to the address book
    book.add_record(john_record)

    # Create and add a new record for Jane
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    # Display all records in the book
    for name, record in book.data.items():
        print(record)

    # Find and edit phone for John
    john = book.find("John")
    if john:
        john.edit_phone("1234567890", "1112223333")
        print(john) # Output: Contact name: John, phones: 1112223333; 5555555555

    # Find a specific phone in John's record
    found_phone = john.find_phone("5555555555")
    print(f"{john.name}: {found_phone}") # Output: John: 5555555555

    # Delete Jane's record
    book.delete("Jane")

    # Display all records in the book
    for name, record in book.data.items():
        print(record) #Contact name: John, phones: 1112223333; 5555555555