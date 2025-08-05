phonebook = {"Mix": "777-1111", "Au": "777-2222", "Bank": "777-3333", "Tle": "777-4444"}

heroesdict = {}
heroesdict["Hulk"] = "888-1111"
heroesdict["Iron Man"] = "888-2222"
print(heroesdict.get("Halk", "key not found"))
print(heroesdict.get("Hulk", "key not found"))

for key, value in phonebook.items():
    print(key, value)

print(phonebook.keys())
print(phonebook.values())

print(phonebook.pop("Mick", "Eement not found"))
print(phonebook.pop("Au", "Element nt found"))
print(phonebook)
print(phonebook.popitem())
print(phonebook)
phonebook.clear()
print("After clear")
print(phonebook)

