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


with open("sales.txt", "r") as sales_file:
    # วนลูปอ่าน ทีละบรรทัด โดย line จะเป็น สตริง เช่น "100.5\n"
    for line in sales_file:
        #แปลงสตริงให้เป็น float เพื่อเอาไปคำนวณต่อได้
        amount = float(line) 
        print(f"{amount:.2f}") 