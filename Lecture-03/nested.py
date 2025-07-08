inchar = input("Input one character:")
if inchar >= 'A' and inchar <= 'z':
    print ("You in put uper Case Letter ", inchar)
elif inchar >= 'a' and inchar <= 'z':
    print("You in put Lower Case Letter ", inchar)
elif inchar >= '0' and inchar <= '9':
    print("You in put Number ", inchar)
else:
    print("It's not a letter or number.",inchar)