phonebook = {"Mix": "777-1111", "Au": "777-2222", "Bank": "777-3333"}

print(phonebook)

print(phonebook["Mix"])
print(phonebook.get("Bank"))

key = "Pong"
if key in phonebook:
    print(phonebook["Pong"])
else:
    print(key + " not in phonebook")

phonebook["Simpson"] = "777-4567"
phonebook["Pong"] = "777-4444"
phonebook["Mickey"] = "777-2122"

del phonebook["Simpson"]
print(phonebook)