from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    # Зберігає об'єкт Name у атрибуті name (успадковано від Field)
    def __init__(self, value):
        super().__init__(value)
        # self.name = value  # для явної відповідності опису

class Phone(Field):
    # Зберігає об'єкт Phone у атрибуті value та реалізує валідацію
    def __init__(self, value):
        if self._validate(value):
            super().__init__(value)
        else:
            raise ValueError("Phone number must contain exactly 10 digits.")

    def _validate(self, value):
        if str(value).isdigit() and len(str(value)) == 10:
            return True
        else:
            return False
        #digits = ''.join(filter(str.isdigit, str(value)))
        #return len(digits) == 10

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
    
    def add_phone(self, phone):
        phone_obj = Phone(phone)
        self.phones.append(phone_obj)

    def find_phone(self, target_phone):
        for i in self.phones:
         if i.value == target_phone:
          return i 

    def remove_phone(self, phone):
        phone_obj = self.find_phone(phone)
        if phone_obj:
            self.phones.remove(phone_obj)
        else:
            raise ValueError(f"Phone number '{phone}' not found.")

    def edit_phone(self, old_phone, new_phone):
        if self.find_phone(old_phone):
            self.add_phone(new_phone)
            self.remove_phone(old_phone)
        else:
            raise ValueError(f"Phone number '{old_phone}' not found.")
       
    # Реалізовано зберігання об'єкта Name в атрибуті name.
    # Реалізовано зберігання списку об'єктів Phone в атрибуті phones.
    # Реалізовано метод для додавання - add_phone .На вхід подається рядок, який містить номер телефона.
    # Реалізовано метод для видалення - remove_phone. На вхід подається рядок, який містить номер телефона.
    # Реалізовано метод для редагування - edit_phone. На вхід подається два аргумента - рядки, які містять старий номер телефона та новий. У разі некоректності вхідних даних метод має завершуватись помилкою ValueError.
    # Реалізовано метод для пошуку об'єктів Phone - find_phone. На вхід подається рядок, який містить номер телефона. Метод має повертати або об’єкт Phone, або None .

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):

    def __str__(self):
        return '\n'.join(f"{key}: {value}" for key, value in self.data.items())
      
    def add_record(self, record):
        self.data[record.name.value] = record
    
    def find(self, name: str):
        return self.data.get(name) 
        
    def delete(self, name: str):
        del self.data[name]
        
    # Має наслідуватись від класу UserDict .
    # Реалізовано метод add_record, який додає запис до self.data. Записи Record у AddressBook зберігаються як значення у словнику. В якості ключів використовується значення Record.name.value.
    # Реалізовано метод find, який знаходить запис за ім'ям. На вхід отримує один аргумент - рядок, якій містить ім’я. Повертає об’єкт Record, або None, якщо запис не знайден.
    # Реалізовано метод delete, який видаляє запис за ім'ям.
    # Реалізовано магічний метод __str__ для красивого виводу об’єкту класу AddressBook .

book = AddressBook()


john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")


book.add_record(john_record)

jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

# Виведення всіх записів у книзі
     
print(book)
#print(john_record)

# Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("1234567890", "1112223333")

print(john)

found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")

book.delete("Jane")

