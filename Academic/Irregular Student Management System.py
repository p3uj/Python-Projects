from os import system
from msvcrt import getch

def login():
    print("LOGIN")

def create_account():
    system("cls")
    print("CREATE ACCOUNT")
    print("Press any key to go back to main...", end='', flush=True)
    getch()

def choices():
    print("1. Create Another Account")
    print("2. Login Account")
    print("3. Exit")

def main():
    print("1. Create Account")
    print("2. Exit")
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