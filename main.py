from functions import add, sub, mul, div, power, area

print("Simple Console Calculator\n\n")

print("1. Addition\n2. Subtraction\n3. Multiply\n4. Divide\n5. Power\n6. Area\n7. Volume\n0. Quit")
choice = int(input("Enter your choice: "))

while choice != 0:
    while choice not in {1, 2, 3, 4, 5, 6, 7}:
        print("\n\nInvalid Choice\n")
        print("1. Addition\n2. Subtraction\n3. Multiply\n4. Divide\n5. Power\n6. Area\n7. Volume\n0. Quit")
        choice = int(input("Enter your choice: "))

    if choice == 1:
        add()
    elif choice == 2:
        sub()
    elif choice == 3:
        mul()
    elif choice == 4:
        div()
    elif choice == 5:
        power()
    elif choice == 6:
        area()
    elif choice == 7:
        pass

    print("\n\n1. Addition\n2. Subtraction\n3. Multiply\n4. Divide\n5. Power\n6. Area\n7. Volume\n0. Quit")
    choice = int(input("Enter your choice: "))

else:
    print("Thank you for using our simple console calculator\nGoodbye!!!")
    exit(0)
