def is_armstrong(number):
    num_str = str(number) # แปลงเลขเป็น string เพื่อเข้าถึงแต่ละหลัก
    num_digits = len(num_str) # นับจำนวนหลัก
    total = 0 #เริ่มต้นผลรวมที่ 0
    for digit in num_str: # วนลูปผ่านแต่ละหลัก
        total += int(digit) ** num_digits # ยกกำลังแล้วบวกเข้า total
    return total == number #เปรียบเทียบกับเลขเดิม

print(is_armstrong(153))
print(is_armstrong(9474))
print(is_armstrong(123))

# คืออะไร I ไม่รู้จัก I รู้จักแต่ นิว อาร์มสตรอง 