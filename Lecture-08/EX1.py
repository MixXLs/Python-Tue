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

with open("employees.txt", "r") as emp_file:
    lines = emp_file.readlines()

    for i in range(0, len(lines), 3):  # len(lines) → คือจำนวนบรรทัดทั้งหมดในไฟล์
        name = lines[i].strip()  # i บรรทัดที่1
        emp_id = lines[i + 1].strip()  # i+1 บรรทัดที่ 2
        dept = lines[i + 2].strip()  # i+2 บรรทัดที่ 3

        print(f"Name: {name}")
        print(f"ID number: {emp_id}")
        print(f"Department: {dept}\n")
