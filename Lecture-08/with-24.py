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

with open("example.txt","r") as file:
    lines = file.readlines()    #อ่าน ทุกบรรทัดทั้งหมดเก็บใน list ก่อน แล้วจึงวนลูป
    for line in lines:          #อ่านข้อความทั้งหมด เหมาะกับไฟล์ที่ไม่ใหญ่มาก
        print(line.strip()) 
