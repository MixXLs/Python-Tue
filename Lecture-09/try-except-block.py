try:
    x = 1 / 0
    d = 6 / 2
except ZeroDivisionError as e:
    print(f"Error: {e}")
print("End of program")
