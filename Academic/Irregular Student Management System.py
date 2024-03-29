from os import system
from msvcrt import getch
accounts_created = {}

def login():
    system("cls")
    print("────────────────────────────────────────────────────────────────────────────────")
    print("LOGIN ACCOUNT".center(80))
    print("────────────────────────────────────────────────────────────────────────────────")

def create_account():
    system("cls")
    print("────────────────────────────────────────────────────────────────────────────────")
    print("CREATE ACCOUNT".center(80))
    print("────────────────────────────────────────────────────────────────────────────────")
    
    user_name = input("Create username: ")
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


def choices():
    print("1. Create Another Account")
    print("2. Login Account")
    print("3. Exit")

def main():
    print("────────────────────────────────────────────────────────────────────────────────")
    print("Irregular Student Management System".center(80))
    print("────────────────────────────────────────────────────────────────────────────────")
    print("(1) Create Account".center(40) + "|" + "(2) Exit".center(39))
    print("────────────────────────────────────────────────────────────────────────────────")
    
    # Initial menu
    while True:
        try:
            choice = int(input("Enter choice: "))
            if choice == 1:
                create_account()
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
                case 1: create_account()
                case 2: login()
                case 3: exit("Program end!")
                case _: print("Invalid choice!")
        except ValueError:
            print("\nInvalid input!")

main()