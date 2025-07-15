columns = int(input("How many columns? "))
while rows > 0 and columns >0 :
    for i in range(1, 101):
        for c in range(columns):
            print(i,end='\t')
        print()
    break
            