# 'r' : อ่าน
# 'w' : เขียน
# 'a' : เพิ่มข้อมูล
# 'b' : โหมดไบนารี
# 't' : โหมดข้อความ
# '+' : อ่าน/เขียน
# file.close()
# with statement: ปิดไฟล์อัตโนมัติ
# read(): อ่านทั้งไฟล์
# readline(): อ่านที่ละบรรทัด
# readlines(): อ่านทุกบรรทัด 
# file.write(): เขียนไฟล์

with open("example.txt", "r") as file:
    line = file.readline()                  #อ่านที่ละบรรทัด
    while line:                             #รันต่อไปเรื่อยๆ จนกว่าข้อความจะหมด
        print(line.strip())                 #.strip() ลบอักขระพิเศษ เช่น \n
        line = file.readline()