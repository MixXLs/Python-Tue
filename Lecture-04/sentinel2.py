rows = int(input("How many rows? "))
columns = int(input("How many columns? "))
while rows > 0 and columns >0 :
    for r in range(rows):
        for c in range(columns):
            print('*',end='')
        print()
    break
            