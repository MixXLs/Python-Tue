# i: จำนวนเต็ม 4ไบต์ (32บิต) ใช้สำหรับฟิลด์ ID และ Age 
# 20s: แทนสตริงขนาด 20ไบต์ ตัว s หมายถึงสตริง ถ้าสตริงสั่นกว่า 20 เติม null (\x00) ถ้ายากกว่าถูกตัดทิ้ง
# f: ทศนิยม 4 ไบต์

import struct

with open("records.bin", "rb") as file:
    record_size = struct.calcsize('i20sif')
    while True:
        data = file.read(record_size)
        if not data:
            break
        record = struct.unpack('i20sif', data)
        '''record = (record[1], record[1].decode().strip(), record[2], record[3])'''
        print(f"ID: {record[0]}, Name: {record[1].decode().strip()}, Age: {record[2]}, GPA: {record[3]}")
