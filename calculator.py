




def calculator():
    while True:
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Quit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))
            print(a + b)
        elif choice == 2:
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))
            print(a - b)
        elif choice == 3:
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))
            print(a * b)
        elif choice == 4:
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))
            print(a / b)
            

