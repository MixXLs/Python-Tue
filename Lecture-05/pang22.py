def print_all(*args): #*args คือ ตัวแปรที่รับค่าได้ไม่จำกัดจำนวน
    for index, arg in enumerate(args):  #index = ตำแหน่งของค่าภายในลิสต์ #enumerate() เป็นฟังก์ชันใน Python ที่ใช้ วนลูปลิสต์หรือชุดข้อมูลอื่นๆ แล้วให้ทั้ง ‘ลำดับ (index)’ และ ‘ค่า (args)’ กลับมาในแต่ละรอบ
        print(f"Argument {index + 1}: {arg}")

print_all("Python", 3.8, True, [1, 2, 3], {"key": "value"})