print("Please select opration -")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
opration = input("from 1, 2, 3, 4 : ")
if opration == "1":
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print(num1, "+", num2, "=", num1 + num2)
elif opration == "2":
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print(num1, "-", num2, "=", num1 - num2)
elif opration == "3":
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print(num1, "*", num2, "=", num1 * num2)
elif opration == "4":
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    if num2 == 0:
        print("Error! Division by zero.")
    else:
        print(num1, "/", num2, "=", num1 / num2) 