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

#อยากบันทึกยอดขายกี่วัน
num_days = int(input("For how many days do you have sales? ")) 
#เปิดไฟล์ชื่อ sales.txt ในโหมด เขียน
with open("sales.txt", "w") as sales_file:  
    #นับจาก 1 ถึง ที่อินพุตเข้ามา
    for count in range(1, num_days +1):  
        #รับค่าตัวเลขยอดขายของแต่ละวัน (เก็บเป็น float)
        sales = float(input(f"Enter the sales for day #{count}: "))
        #แปลง float เป็น str ก่อบันทึกลงไฟล์
        sales_file.write(str(sales) + '\n')