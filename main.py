from datetime import datetime, date, timedelta
from collections import UserDict
import pickle


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self,value):
        if not value:
            raise ValueError('Name cannot be empty')
        super().__init__(value)
           

class Phone(Field):
    def __init__(self, value):
        self.validate(value)
        super().__init__(value)

    def validate(self, value):
        if len(value) != 10 or not value.isdigit():
            raise ValueError("Phone number must contain exactly 10 digits")
        
class Birthday(Field):
    def __init__(self, value):
        try:
            birthday = datetime.strptime(value, "%d.%m.%Y")
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")
        if birthday > datetime.now():
            raise ValueError("Error! Birthday date cannot be later than today")

        self.value = datetime.strftime(birthday, '%d.%m.%Y')
    def __str__(self):
        return self.value

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    # метод додавання номера телефону.
    def add_phone(self,phone):
        self.phones.append(Phone(phone))

    # метод видалення номера телефону.
    def remove_phone(self,phone):
        searched_phone = self.find_phone(phone)
        if searched_phone:
            self.phones.remove(searched_phone)
        else:
            raise ValueError(f"{phone} is not found")

    # метод редагування номера телефону.
    def edit_phone(self,old_phone,new_phone):
        searched_phone = self.find_phone(old_phone)
        if searched_phone:
            searched_phone.value = Phone(new_phone).value
        else:
            raise ValueError(f'{old_phone} is not found')

    # метод пошуку об'єктів Phone
    def find_phone(self,phone):
        found_phone = next(filter(lambda item: item.value == phone, self.phones), None)
        return found_phone
    
    def add_birthday(self, birthday):
        self.birthday = Birthday(birthday)

    def show_birthday(self):
        return self.birthday
    

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}, birthday: {self.birthday.value if self.birthday is not None else 'Unknown'}"

class AddressBook(UserDict):
    # метод додає запис до self.data.
    def add_record(self, record):
        self.data[record.name.value] = record
    
    # метод знаходить запис за ім'ям.
    def find(self,name):
        return self.data.get(name)
    
    #метод видаляє запис за ім'ям
    def delete(self, name):
        if name in self.data:
            self.data.pop(name)

    def date_to_string(self,date):
        return date.strftime("%d.%m.%Y")
    
    def find_next_weekday(self,start_date, weekday):
        days_ahead = weekday - start_date.weekday()
        if days_ahead <= 0:
            days_ahead += 7
        return start_date + timedelta(days=days_ahead)


    def adjust_for_weekend(self,birthday):
        if birthday.weekday() >= 5:
            return self.find_next_weekday(birthday, 0)
        return birthday

    def get_upcoming_birthdays(self, days=7):
        upcoming_birthdays = []
        today = date.today()
    
        for name, record in self.data.items():
            if record.birthday is None:
                continue
            birthday_this_year_str = record.birthday.value
            birthday_this_year_date = datetime.strptime(birthday_this_year_str, '%d.%m.%Y').date()
            try: 
                birthday_this_year = birthday_this_year_date.replace(year=today.year)
            except ValueError:
                birthday_this_year = birthday_this_year_date.replace(year=today.year, day=28)
                
    
            if birthday_this_year < today:
                birthday_this_year= birthday_this_year.replace(year=today.year+1)
    
            if 0 <= (birthday_this_year - today).days <= days:
                birthday_this_year = self.adjust_for_weekend(birthday_this_year)
                congratulation_date_str = self.date_to_string(birthday_this_year)
                upcoming_birthdays.append({"name": name, "birthday": congratulation_date_str})
        return upcoming_birthdays

    def __str__(self):
        lines = [str(record) for record in self.data.values()]
        return "\n".join(lines) if lines else "Address book is empty."
    

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as e:
            return str(e)
        except IndexError:
            return "Enter user name"
        except KeyError:
            return "Username not found."
        except AttributeError:
            return "User is not found"

    return inner

def parse_input(user_input):
    if not user_input.strip():
        raise ValueError("Please, enter value")
        
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, book: AddressBook):
    name, phone, *_ = args
    record = book.find(name)
    message = "Contact updated."
    if record is None:
        Phone(phone)
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
    if phone:
        record.add_phone(phone)
    return message


@input_error
def change_contact(args, book: AddressBook):
    name, old_phone, new_phone, *_ = args 
    record = book.find(name)
    record.edit_phone(old_phone, new_phone)
    return f"The phone number for user {name} has been updated to {new_phone}"
        

@input_error
def show_phone(args, book: AddressBook):
    name, *_ = args
    record = book.find(name)
    return "; ".join(p.value for p in record.phones)
   

def show_all(args, book:AddressBook):
    return f'{book}'

@input_error
def add_birthday(args,book:AddressBook):
    name, birthday, *_ = args
    record = book.find(name)
    record.add_birthday(birthday)
    return f'Birthday date for user {name} is added'


@input_error  
def show_birthday(args,book: AddressBook):
    name, *_ = args
    record = book.find(name)
    user_birthday = record.show_birthday()
    if user_birthday is None:
        return f"{name}'s birthday has not been added yet"
    return user_birthday


@input_error   
def birthdays(args,book:AddressBook):
    upcoming = book.get_upcoming_birthdays()
    if not upcoming:
        return "No birthdays in the next 7 days."
    return "\n".join(f"{user['name']}: {user['birthday']}" for user in upcoming)


def save_data(book, filename="addressbook.pkl"):
    with open(filename, "wb") as f:
        pickle.dump(book, f)

def load_data(filename="addressbook.pkl"):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return AddressBook()  # Повернення нової адресної книги, якщо файл не знайдено



def main():
    book = load_data()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        try:
            command, *args = parse_input(user_input)
        except ValueError as e:
            print(e)
            continue

        if command in ["close", "exit"]:
            save_data(book)
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(add_contact(args, book))

        elif command == "change":
            print(change_contact(args,book))

        elif command == "phone":
            print(show_phone(args, book))

        elif command == "all":
            print(show_all(args,book))

        elif command == "add-birthday":
            print(add_birthday(args,book))

        elif command == "show-birthday":
            print(show_birthday(args,book))

        elif command == "birthdays":
            print(birthdays(args,book))
        else:
            print("Invalid command.")
    

if __name__ == "__main__":
    main()