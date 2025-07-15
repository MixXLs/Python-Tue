columns = int(input("How many columns? "))
for i in range(1,101):
    print (i ,end="\t")
    if i % columns == 0:
        print()

