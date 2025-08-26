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
# file.write(): เขียนไฟล์ ``

num_emps = int(input("How many employee records do you want to create? "))
#เปิดไฟล์สำหรับเขียน (เขียนทับไฟล์เก่า)
with open("employees.txt", "w") as emp_file:
    #วนลูปตามจำนวนพนักงาน
    for count in range(1, num_emps +1):
        print("Enter data for employee #", count, sep='')
        name = input('Name: ') 
        id_num = input('ID number: ')
        dept = input('Department: ')

        emp_file.write(name + '\n')
        emp_file.write(id_num + '\n')
        emp_file.write(dept + '\n')
        print()

print("Employee records written to employees.txt")