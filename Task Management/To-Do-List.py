def main():
    global created, toDo, os
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
            exit("THANK YOU FOR USING MY PROGRAM!".center(50))
        else:
            print("WARNING: INVALID CHOICE!")


def addList(c):
    con = "Y"
    num = 1

    print("1. ADD LIST".center(50))
    print("NOTE: Enter \"!\" to END the creating of a list!")

    task = input(f"{num}. [ ] ").strip()
    if task[0] != "!":
        toDo.append("[ ] " + task)
        c = 1
    while task[0] != "!":
        num += 1
        task = input(f"{num}. [ ] ").strip()
        if task[0] != "!":
            toDo.append("[ ] " + task)
    
    # Printing the the created list
    num = 1
    print("\nTO-DO LIST:")
    if len(toDo) != 0:
        for task in toDo:
            print(f"{num}. {task}")
            num += 1
    else:
        print("No record/s")
    
    while con != "Y" or con != "N":
        con = input("\nDo you want to continue this program? (Y/N): ").strip().upper()
        if con == "N":
            os.system("cls")
            exit("THANK YOU FOR USING MY PROGRAM!".center(50))
        elif con == "Y":
            os.system("cls")
            return c
        else:
            print("WARNING: INVALID CHOICE!")


main()