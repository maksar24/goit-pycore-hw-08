from address_book import AddressBook
from commands import add_contact, change_phone, show_phone, show_all_contacts, add_birthday, show_birthday, birthdays

def main():
    book = AddressBook()
    print("Welcome to the bot assistant!")

    while True:
        user_input = input("Enter command: ")
        command, *args = user_input.split()

        if command in ["close", "exit"]:
            print("Goodbye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, book))
        elif command == "change":
            print(change_phone(args, book))
        elif command == "phone":
            print(show_phone(args, book))
        elif command == "all":
            print(show_all_contacts(book))
        elif command == "add-birthday":
            print(add_birthday(args, book))
        elif command == "show-birthday":
            print(show_birthday(args, book))
        elif command == "birthdays":
            print(birthdays(book))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()