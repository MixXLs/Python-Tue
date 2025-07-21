def find_max(*args): #หาค่ามากที่สุด
    if not args: #ถ้าไม่มีการส่งค่ามา(args)ให้คืนค่าNone
        return None
    max_value = args[0] #ใช้ ค่าตัวแรก ที่ผู้ใช้ส่งเข้ามาใน *args เพื่อเป็น จุดเริ่มต้นในการเปรียบเทียบหาค่าสูงสุด
    for number in args:
        if number > max_value:
            max_value = number
    return max_value

result = find_max(3, 5, 7, 2, 8)
print(f"The maximum value is: {result}")