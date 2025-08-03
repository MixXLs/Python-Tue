heroes = ['Ironman', 'Thor', 'Hulk', 'Spiderman']
print(heroes)
heroes.append(input("Enter Hero :"))
heroes.insert(int(input("Enter len :")),str(input("Enter Hero Insert :")))
heroes.remove(input("Remove Hero :"))
heroes.sort()
print(heroes)
heroes.reverse()
print(heroes)