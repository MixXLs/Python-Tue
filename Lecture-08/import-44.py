# i: จำนวนเต็ม 4ไบต์ (32บิต) ใช้สำหรับฟิลด์ ID และ Age 
# 20s: แทนสตริงขนาด 20ไบต์ ตัว s หมายถึงสตริง ถ้าสตริงสั่นกว่า 20 เติม null (\x00) ถ้ายากกว่าถูกตัดทิ้ง
# f: ทศนิยม 4 ไบต์

import struct

record_fomat = 'i20sif'
record_size = struct.calcsize(record_fomat)

with open("records.bin", "rb") as file:
    # seek เลื่อนไปหนึ่ง record
    file.seek(record_size)
    data = file.read(record_size)
    record = struct.unpack(record_fomat, data)
   
    print(f"ID: {record[0]} Name: {record[1].decode().strip()} Age: {record[2]} GPA: {record[3]}")
