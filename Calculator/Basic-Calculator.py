def userInput():
    print("────────────────────────────────────────────────")
    firstNum = float(input("Enter first number: "))
    secondNum = float(input("Enter second number: "))
    return firstNum, secondNum

def main():
    import os   # To clear the screen
    con = 'Y'

    while con == 'Y' or con == 'y':
        print("────────────────────────────────────────────────")
        print("\t\tBASIC CALCULATOR")
        print("────────────────────────────────────────────────")
        print("\t       ADD   MUL   SUB   DIV")
        print("\t     ─────────────────────────")
        print("\t     ║  +  ║  x  ║  -  ║  ÷  ║")
        print("\t     ─────────────────────────")
        print("\t        1     2     3     4\n")
        choice = int(input("Enter choice: "))

        # Validation of the input
        while choice > 4 or choice < 1:
            choice = int(input("\nWARNING: INVALID CHOICE!\nEnter choice: "))

        os.system("cls")    # Clear the screen
        print("────────────────────────────────────────────────")
        match choice:
            case 1 : 
                print("\t\tADDITION")
                firstNum, secondNum = userInput()
                print(f"\n{firstNum} + {secondNum} = {firstNum + secondNum}")
            case 2 : 
                print("\t\tMULTIPLICATION")
                firstNum, secondNum = userInput()
                print(f"\n{firstNum} x {secondNum} = {firstNum * secondNum}")
            case 3 : 
                print("\t\tSUBTRACTION")
                firstNum, secondNum = userInput()
                print(f"\n{firstNum} - {secondNum} = {firstNum - secondNum}")
            case 4 : 
                print("\t\tDIVITION")
                firstNum, secondNum = userInput()
                print(f"\n{firstNum} ÷ {secondNum} = {firstNum / secondNum}")

        con = input("\nDo you want to continue this program? (Y/N): ")

        # Validation of the input
        while con != 'Y' and con != 'y' and con != 'N' and con != 'n':
            con = input("\nWARNING: INVALID INPUT!\nDo you want to continue this program? (Y/N): ")
        os.system("cls")    # Clear the screen

    print("────────────────────────────────────────────────")
    print("\t\tEND OF THE PROGRAM!")
    print("────────────────────────────────────────────────")

main()