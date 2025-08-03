inventory = [
    ["Apple", 50, 0.75], # [ชื่อสินค้า, จำนวนในคลัง, ราคาต่อชิ้น]
    ["Banana", 100, 0.50],
    ["Orange", 75, 0.80]
]
#ขียนฟังก์ชันชื่อ update_inventory(inventory, item_name, quantity_sold)
#เพื่อ ลดจำนวนสินค้าที่ระบุ หลังจากการขายสินค้า
#เป้าหมาย: ลดจำนวนสินค้าหลังขาย

def update_inventory(inventory, item_name, quantity_sold):
    for item in inventory:
        if item[0] == item_name:
            item[1] -= quantity_sold
            if item[1] <= 0:
                (inventory.remove(item))
            return # ให้ return แค่เมื่อเจอสินค้า
    print(item_name)

def calculate_total_value(inventory):
    total = 0
    for item in inventory:
        total += item[1] * item[2]
    return total

def find_most_expensive(inventory):
    most_expensive = inventory[0]
    for item in inventory:
        if item[2] > most_expensive[2]:
            most_expensive = item
    return most_expensive[0]

def add_item(inventory, item_name, quantity, price):
    for item in inventory:
        if item[0] == item_name:
            item[1] = quantity
            item[2] = price
            return
    inventory.append([item_name, quantity, price])


update_inventory(inventory, "Banana", 20)
print(inventory)

total = calculate_total_value(inventory)
print(total)

print(find_most_expensive(inventory))

add_item(inventory, "Eggs", 30, 0.25)

for item in inventory:
    print(item)

add_item(inventory, "Eggs", 50, 0.30)
print("/nUp-in")
for item in inventory:
    print(item)