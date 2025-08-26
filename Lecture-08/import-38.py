# i: จำนวนเต็ม 4ไบต์ (32บิต) ใช้สำหรับฟิลด์ ID และ Age 
# 20s: แทนสตริงขนาด 20ไบต์ ตัว s หมายถึงสตริง ถ้าสตริงสั่นกว่า 20 เติม null (\x00) ถ้ายากกว่าถูกตัดทิ้ง
# f: ทศนิยม 4 ไบต์

import struct

record = (1, 'john Doe', 20, 3.75)

with open("records.bin", "wb") as file:

    data = struct.pack('i20sif', record[0], record[1].encode(), record[2], record[3])

    file.write(data)