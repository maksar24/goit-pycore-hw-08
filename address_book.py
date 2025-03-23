from collections import UserDict
import re
from datetime import datetime, timedelta

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, value):
        if not value:
            raise ValueError("Name is a required field.")
        super().__init__(value) 

class Phone(Field):
    def __init__(self, value):
        if not re.match(r'^\d{10}$', value):
            raise ValueError("Phone number must be exactly 10 digits.")
        super().__init__(value)

class Birthday(Field):
    def __init__(self, value):
        try:
            self.value = datetime.strptime(value, "%d.%m.%Y")
        except ValueError:
            raise ValueError("Неправильний формат дати. Використовуйте ДД.ММ.РРРР")

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def _find_phone_by_value(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p
        return None

    def remove_phone(self, phone):
        phone_obj = self._find_phone_by_value(phone)
        if phone_obj:
            self.phones.remove(phone_obj)
            return f"Phone {phone} removed."
        return f"Phone {phone} not found."

    def edit_phone(self, old_phone, new_phone):
        phone_obj = self._find_phone_by_value(old_phone)
        if phone_obj:
            phone_obj.value = new_phone
            return f"Phone {old_phone} changed to {new_phone}."
        return f"Phone {old_phone} not found."

    def find_phone(self, phone):
        if self._find_phone_by_value(phone):
            return f"Phone {phone} found."
        return f"Phone {phone} not found."
    
    def add_birthday(self, birthday):
        if not self.birthday:
            self.birthday = Birthday(birthday)
            return f"Birthday {birthday} added for {self.name.value}."
        return f"Birthday for {self.name.value} is already set."

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}, birthday: {self.birthday if self.birthday else 'Not set'}"

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            del self.data[name]
            return f"Record with name {name} has been deleted."
        return f"Record with name {name} not found."
    
    def get_upcoming_birthdays(self):
        current_date = datetime.today().date()
        upcoming_birthdays = []

        for record in self.data.values():
            if record.birthday:
                birthday = record.birthday.value.date()

                birthday_this_year = birthday.replace(year=current_date.year)
                if birthday_this_year < current_date:
                    birthday_this_year = birthday_this_year.replace(year=current_date.year + 1)

                if current_date <= birthday_this_year <= current_date + timedelta(days=7):
                    if birthday_this_year.weekday() >= 5: 
                        days_to_monday = 7 - birthday_this_year.weekday()
                        birthday_this_year += timedelta(days=days_to_monday)

                    upcoming_birthdays.append({
                        "name": record.name.value,
                        "congratulation_date": birthday_this_year.strftime("%Y.%m.%d")
                    })

        return upcoming_birthdays