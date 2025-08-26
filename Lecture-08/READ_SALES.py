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
# file.write(): เเขียนไฟล์

with open("sales.txt","r") as sales_file:
    line = sales_file.readline()
    #ตรวจสอบ ถ้าเป็นสตริงว่าง '' ให้ออกจากloop
    while line != '': 
        # แปลงข้อความเป็นfloat
        amount = float(line) 
        print(f"{amount:.2f}")
        # อ่านบรรทัดถัดไปแล้ววน loop ต่อ
        line = sales_file.readline() 