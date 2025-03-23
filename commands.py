# commands.py
from decorators import input_error
from address_book import Record

@input_error
def add_contact(args, book):
    name, phone, *_ = args
    record = book.find(name)
    message = "Contact updated."
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
    if phone:
        record.add_phone(phone)
    return message

@input_error
def change_phone(args, book):
    name, old_phone, new_phone = args
    record = book.find(name)
    if record is None:
        return "Contact not found."
    return record.edit_phone(old_phone, new_phone)

@input_error
def show_phone(args, book):
    name = args[0]
    record = book.find(name)
    if record is None:
        return "Contact not found."
    return ', '.join(phone.value for phone in record.phones)

@input_error
def show_all_contacts(book):
    if not book.data:
        return "There are no contacts in the address book."
    return "\n".join(str(record) for record in book.data.values())

@input_error
def add_birthday(args, book):
    name, birthday = args
    record = book.find(name)
    if record is None:
        return "Contact not found."
    return record.add_birthday(birthday)

@input_error
def show_birthday(args, book):
    name = args[0]
    record = book.find(name)
    if record is None:
        return "Contact not found."
    return record.birthday.value if record.birthday else "Birthday not set."

@input_error
def birthdays(book):
    upcoming_birthdays = book.get_upcoming_birthdays()
    if not upcoming_birthdays:
        return "No birthdays upcoming in the next week."
    result = "Upcoming birthdays:\n"
    for user in upcoming_birthdays:
        result += f"{user['name']} - {user['congratulation_date']}\n"
    return result
