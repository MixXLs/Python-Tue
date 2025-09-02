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

#เขียนข้อความ
with open("example.txt", "w") as file: 
    file.write("Hello world!\n")
    file.write("This is a new line.\n")

#เพิ่มข้อความ
with open("example.txt", "a") as file: 
    file.write("This line is appended.\n")

#อ่านข้อความ
with open("example.txt", "r") as file: 
    contents = file.read()
    print(contents)