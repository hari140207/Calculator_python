print("Welcome to Calculator")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("1.Add 2.Subtract 3.Multiply 4.Divide")
choice = input("Enter choice: ")

if choice == "1":
    print(num1 + num2)
elif choice == "2":
    print(num1 - num2)
elif choice == "3":
    print(num1 * num2)
elif choice == "4":
    print(num1 / num2)
else:
    print("Invalid choice")