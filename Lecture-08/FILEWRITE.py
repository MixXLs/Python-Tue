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

def main():
    outfile = open("philosophers.txt" , "w") #เขียนข้อความ

    outfile.write("John Locke\n")
    outfile.write("Devid Hume\n")
    outfile.write("Edmund Burke\n")

    outfile.close()
main()