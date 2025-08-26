import struct

num_records = int(input("How many records do you want to create? "))

with open("records.bin", "wb") as file:  # สร้างไฟล์ไบนารี
    for _ in range(num_records):
        id_num = int(input("Enter ID: "))
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        gpa = float(input("Enter GPA: \n"))

        #i20sif คือ i เลขจำนวนเต็ม4ไบต์ 20s สตริงขนาด 20 ไบต์ f  float 4 ไบต์
        data = struct.pack('i20sif', id_num, name.encode(), age, gpa)  
        file.write(data)

print(f"{num_records} recode have been written to records.bin")