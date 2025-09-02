# i: จำนวนเต็ม 4ไบต์ (32บิต) ใช้สำหรับฟิลด์ ID และ Age 
# 20s: แทนสตริงขนาด 20ไบต์ ตัว s หมายถึงสตริง ถ้าสตริงสั่นกว่า 20 เติม null (\x00) ถ้ายากกว่าถูกตัดทิ้ง
# f: ทศนิยม 4 ไบต์

import struct

num_records = int(input("How many records do you want to create? "))

with open("records.bin", "wb") as file:  # สร้างไฟล์ไบนารี
    for _ in range(num_records):
        id_num = int(input("Enter ID: "))
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        gpa = float(input("Enter GPA: "))
        print("-"*20)
        
        data = struct.pack('i20sif', id_num, name.encode(), age, gpa)  
        file.write(data)

print(f"{num_records} recode have been written to records.bin")