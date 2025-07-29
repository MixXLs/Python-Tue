heroes = ['Ironman', 'Thor', 'Hulk', 'Spiderman']
#with:
print(heroes)
heroes.append(input("Enter Hero :"))
print(heroes)
heroes.insert(int(input("Enter len :")),str(input("Enter Hero :")))
print(heroes) 
heroes.remove(input("Remove Hero :"))
print(heroes)
heroes.sort()
print(heroes)
heroes.reverse()
print(heroes)