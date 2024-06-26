from os import system
from msvcrt import getch
accounts_created = {}

def login(title):
    has_warning_message = False
    system("cls")
    header_page(title)

    user_name = input("Username: ")
    
    # Validate if the username is already created.
    while user_name not in accounts_created:
        has_warning_message = True
        system("cls")
        header_page(title)
        print("(1) Try again".center(26) + "|" + "(2) Create Account".center(26) + "|" + "(3) Exit".center(26))
        print("────────────────────────────────────────────────────────────────────────────────")
        print("USERNAME IS NOT YET CREATED!".center(80))
        while True:
            try:
                choice = int(input("Enter choice: "))
                match choice:
                    case 1: user_name, password = login("LOGIN ACCOUNT")
                    case 2: create_account("CREATE ACCOUNT")
                    case 3: exit("Program End!")
                    case _: print("Invalid choice!")
                break
            except ValueError:
                print("\nInvalid input! Please enter integer only!")
    if has_warning_message:
        system("cls")
        header_page(title)
        print(f"Username: {user_name}")
        has_warning_message = False

    password = input("Enter password: ")

    # Validate if the entered password is match to the created password.
    while accounts_created[user_name] != password:  # Loop as long as the entered password is not match to the created password.
        system("cls")
        header_page(title)
        print("(1) Try again".center(40) + "|" + "(2) Exit".center(39))
        print("────────────────────────────────────────────────────────────────────────────────")
        print("INCORRECT PASSWORD!".center(80))
        while True:
            try:
                choice = int(input("Enter choice: "))
                if choice == 1:
                    system("cls")
                    header_page(title)
                    password = input("Enter password: ")
                    break
                elif choice == 2:
                    exit("Program end!")
                else:
                    print("Invalid choice!")
            except ValueError:
                print("\nInvalid input! Please enter integer only!")
    print("Successfully login!")
    print("\t\t\tPress any key to go back to main...", end='', flush=True)
    getch()
    return user_name, password

def create_account(title):
    has_warning_message = False
    system("cls")
    header_page(title)

    user_name = input("Create username: ")

    # Validate if the user name is already used.
    while user_name in accounts_created:
        has_warning_message = True
        system("cls")
        header_page(title)
        print("USERNAME ALREADY USED! PLEASE USE DIFFERENT USERNAME!".center(80))
        user_name = input("Create username: ")
    if has_warning_message:
        system("cls")
        header_page(title)
        print(f"Create username: {user_name}")
        has_warning_message = False

    # Validate the length of the user name
    while len(user_name) < 8 or len(user_name) > 16: # Loop as long as the length of the username is less than 8 or greater than 16.
        has_warning_message = True
        system("cls")
        header_page(title)
        print("USERNAME MUST BE 8 CHARACTERS AND NOT EXCEED TO 16!".center(80))
        user_name = input("Create username: ")
    if has_warning_message:
        system("cls")
        header_page(title)
        print(f"Create username: {user_name}")
        has_warning_message = False

    password = input("Create password: ")

    # Validate the length of the password.
    while len(password) < 8: # Loop as long as the length of the password is less than 8.
        system("cls")
        header_page(title)
        print("PASSWORD MUST BE 8 CHARACTERS OR MORE!".center(80))
        password = input("Create password: ")

    accounts_created[user_name] = password  # Adding the created username and password to the accounts_created(dict).

    system("cls")
    print("────────────────────────────────────────────────────────────────────────────────")
    print("CREATE ACCOUNT".center(80))
    print("────────────────────────────────────────────────────────────────────────────────")

    print("C O N G R A T U L A T I O N S !".center(80))
    print("Account successfully created!\n".center(80))
    print(f"Username: {user_name}".center(80))
    print(f"Password: {password}\n".center(80))
    print("\t\t\tPress any key to go back to main...", end='', flush=True)
    getch()

def header_page(title_page):
    print("────────────────────────────────────────────────────────────────────────────────")
    print(f"{title_page}".center(80))
    print("────────────────────────────────────────────────────────────────────────────────")
    match title_page:
        case "Irregular Student Management System":
            print("(1) Create Account".center(40) + "|" + "(2) Exit".center(39))
        case "CREATE ACCOUNT":
            print("R E Q U I R E M E N T S !".center(80))
            print("\tUSERNAME - Minimum of 8 characters and maximum of 16 characters only!")
            print("\tPASSWORD - Minimum of 8 characters!")
    print("────────────────────────────────────────────────────────────────────────────────")

def choices():
    print("1. Create Another Account")
    print("2. Login Account")
    print("3. Exit")

def main():
    header_page("Irregular Student Management System")
    
    # Initial menu
    while True:
        try:
            choice = int(input("Enter choice: "))
            if choice == 1:
                create_account("CREATE ACCOUNT")
            else:
                exit("Program end!")
            break
        except ValueError:
            print("\nInvalid input! Please input an integer only!")

    # Main menu
    while True:
        try:
            system("cls")
            choices()
            choice = int(input("Enter choice: "))
            match choice:
                case 1: create_account("CREATE ACCOUNT")
                case 2: login("LOGIN ACCOUNT")
                case 3: exit("Program end!")
                case _: print("Invalid choice!")
        except ValueError:
            print("\nInvalid input!")

main()