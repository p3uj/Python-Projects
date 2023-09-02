def main():
    global created, toDo, os, choice
    import os   # Module to work the clearscreen.
    created = 0
    toDo = []
    while not created:
        print("1. Add List")
        print("2. Exit")
        choice = int(input("Enter choice: "))
        os.system("cls")
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
            os.system("cls")
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
    con = "Y"

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
        print("No record/s")
    
    if choice==1 or choice==2:
        while con != "Y" or con != "N":
            con = input("\nDo you want to continue this program? (Y/N): ").strip().upper()
            if con == "N":
                os.system("cls")
                exit("-" * 50 + "\n" + "THANK YOU FOR USING MY PROGRAM!".center(50) + "\n" + "-" * 50)
            elif con == "Y":
                os.system("cls")
                break
            else:
                print("WARNING: INVALID CHOICE!")


def deleteList():
    con = "Y"

    print("-" * 50)
    print("3. DELETE LIST".center(50))
    print("-" * 50)

    viewList()
    if len(toDo) != 0:
        while True:
            try:
                delete = int(input("Enter a number to be deleted: "))
                if len(toDo) <= delete or delete > 0:
                    toDo.remove(toDo[delete - 1])
                    viewList()
                    break
                else:
                    print(f"\n{delete} is not in the list!-")    # Display this if the number to be deleted is a negative.
            except IndexError:
                print(f"\n{delete} is not in the list!")    # Display this if the number to be deleted is not in the list/out of range.

    while con != "Y" or con != "N":
        con = input("\nDo you want to continue this program? (Y/N): ").strip().upper()
        if con == "N":
            os.system("cls")
            exit("-" * 50 + "\n" + "THANK YOU FOR USING MY PROGRAM!".center(50) + "\n" + "-" * 50)
        elif con == "Y":
            os.system("cls")
            break
        else:
            print("WARNING: INVALID CHOICE!")


def checkMark():
    con = "Y"

    print("-" * 50)
    print("4. CHECK MARK THE LIST".center(50))
    print("-" * 50)

    viewList()
    
    check = int(input("Enter a number to mark as check: "))

    # Check if the item is already marked as checked or not.
    if "[ ]" in toDo[check - 1]:
        toDo[check - 1] = toDo[check - 1].replace("[ ]", "[✓]")
    else:
        print(f"The item in {check} is already marked as checked.")

    viewList()

    while con != "Y" or con != "N":
        con = input("\nDo you want to continue this program? (Y/N): ").strip().upper()
        if con == "N":
            os.system("cls")
            exit("-" * 50 + "\n" + "THANK YOU FOR USING MY PROGRAM!".center(50) + "\n" + "-" * 50)
        elif con == "Y":
            os.system("cls")
            break
        else:
            print("WARNING: INVALID CHOICE!")


main()