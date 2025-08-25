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


with open("example.txt", "w") as file: #เขียนข้อความ
    file.write("Hello world!\n")
    file.write("This is a new line.\n")


with open("example.txt", "a") as file: #เพิ่มข้อความ
    file.write("This line is appended.\n")

with open("example.txt", "r") as file: #อ่านข้อความ
    contents = file.read()
    print(contents)