def main():
    global created, toDo, choice, system, getch
    from os import system  # os is the module used to work the system function (clearscreen).
    from msvcrt import getch # msvcrt is the module used to work the getch function.
    created = 0
    toDo = []

    while not created:
        print("1. Add List")
        print("2. Exit")
        choice = int(input("Enter choice: "))
        system("cls")
        if choice == 1:
            created = addList(created)
        elif choice == 2:
            exit("-" * 50 + "\n" + "THANK YOU FOR USING MY PROGRAM!".center(50) + "\n" + "-" * 50)
        else:
            print("WARNING: INVALID CHOICE!")
        while created:
            print("1. Add List")
            print("2. View List")
            print("3. Delete List")
            print("4. Check Mark the List")
            print("5. Exit")
            choice = int(input("Enter choice: "))
            system("cls")
            match choice:
                case 1 : created = addList(created)
                case 2 : viewList()
                case 3 : deleteList()
                case 4 : checkMark()
                case 5 : exit("-" * 50 + "\n" + "THANK YOU FOR USING MY PROGRAM!".center(50) + "\n" + "-" * 50)


def addList(c):
    num = 1

    print("-" * 50)
    print("1. ADD LIST".center(50))
    print("-" * 50)
    print("NOTE: Enter \"!\" to END the creating of a list!\n")

    # Display the created list if there is.
    if created==1:
        print("Created List:")
        for task in toDo:
            print(f"{num}. {task}")
            num += 1
        print("\nAdd List:")
    
    taskInput = input(f"{num}. [ ] ").strip()
    if taskInput[0] != "!":
        toDo.append("[ ] " + taskInput)
        c = 1
    while taskInput[0] != "!":
        num += 1
        taskInput = input(f"{num}. [ ] ").strip()
        if taskInput[0] != "!":
            toDo.append("[ ] " + taskInput)
    
    # Printing the created list/updated list
    viewList()
    return c


def viewList():
    num = 1

    if choice==2:
        print("-" * 50)
        print("2. VIEW LIST".center(50))
        print("-" * 50)
    print("\nTO-DO LIST:")
    if len(toDo) != 0:
        for task in toDo:
            print(f"{num}. {task}")
            num += 1
    else:
        print("No record/s\n")
    
    if choice==1 or choice==2:
        print("Press any key to go back to main...", end='', flush=True) # The end='' is used to stay the cursor in this line. And the flush=True is used to ensure the message will be display before the user enter any key.
        getch()
        system("cls")
    


def deleteList():
    con = 'Y'

    if len(toDo) != 0:
        while con == 'Y' and len(toDo) != 0:    # Outer While Loop.
            system("cls")
            print("-" * 50)
            print("3. DELETE LIST".center(50))
            print("-" * 50)
            viewList()
            while True: # Inner While Loop.
                try:
                    delete = input("Enter a number to be deleted: ") # Initially, delete variable is a string data type so that we still able to display what the user inputted if it can't convert to int.
                    delete = int(delete)    # Convert the string to int.
                    if len(toDo) <= delete or delete > 0:
                        toDo.remove(toDo[delete - 1])
                        viewList()
                        if len(toDo) != 0:  # Check if the updated number of the list is not equal to 0.
                            con = input("\nDo you want to delete another list? (Y/N): ").strip().upper()
                            while con != 'Y' and con != 'N':
                                print("WARNING: INVALID CHOICE!\n")
                                con = input("Do you want to delete another list? (Y/N): ").strip().upper()
                            break   # Break the inner loop.
                        else:
                            print("Press any key to go back to main...", end='', flush=True)
                            getch()
                            break   # Break the inner loop.
                    else:
                        print(f"\n{delete} is not in the list!")    # Display this if the number to be deleted is zero or negative.
                except (IndexError, ValueError):
                    print(f"\n{delete} is not in the list!")    # Display this if the number to be deleted is not in the list/out of range.
    else:
        print("-" * 50 + "\n" + "3. DELETE LIST".center(50) + "\n" + "-" * 50)
        viewList()
        print("Press any key to go back to main...", end='', flush=True)
        getch()
    
    system("cls")


def checkMark():
    con = 'Y'

    if len(toDo) != 0:
        while con == 'Y':
            system("cls")
            print("-" * 50)
            print("4. CHECK MARK THE LIST".center(50))
            print("-" * 50)
            viewList()
            while True:
                try:
                    check = input("Enter a number to mark as check: ")
                    check = int(check)
                    if len(toDo) <= check or check > 0:
                        # Check if the item is already marked as checked or not.
                        if "[ ]" in toDo[check - 1]:
                            toDo[check - 1] = toDo[check - 1].replace("[ ]", "[✓]")
                        else:
                            print(f"The item in the number {check} is already marked as checked.")
                        
                        viewList()
                        con = input("\nDo you want to mark another list as checked? (Y/N): ").strip().upper()
                        while con != 'Y' and con != 'N':
                            print("WARNING: INVALID CHOICE!\n")
                            con = input("\nDo you want ot mark another list as checked? (Y/N): ").strip().upper()
                        break
                    else:
                        print(f"\n{check} is not in the list!")
                except (IndexError, ValueError):
                    print(f"\n{check} is not in the list!")
    else:
        print("-" * 50 + "\n" + "4. CHECK MARK THE LIST".center(50) + "\n" + "-" * 50)
        viewList()
        print("Press any key to go back to main...", end='', flush=True)
        getch()
    
    system("cls")


main()