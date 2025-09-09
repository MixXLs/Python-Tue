try:
    numrator = float(input("Enter the numrator"))
    denominator = float(input("Enter the denominator"))

    result = numrator / denominator
    print(f"The result is: {result}")
except ZeroDivisionError:
    print("Error: you cannot divide by zero.")
except ValueError:
    print("Error: Invalid input Please enter numeric values.")

finally:
    print("Execution completed, whether an exception occurred or not. ")
print("End of program")