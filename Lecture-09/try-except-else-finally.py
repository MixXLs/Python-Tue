try:
    value = int(input("Enter number: "))
    result = 10 / value
except ValueError:
    print("Invalid input! Please enter a number. ")
except ZeroDivisionError:
    print("Cannot divide by zero! ")
else:
    print(f"The result is {result}")
finally:
    print("Execution completed")