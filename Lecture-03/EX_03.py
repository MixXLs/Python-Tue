houre_worked = float(input("Enter the number of hours worked: "))
hourly_rate = float(input("Enter the hourly rate: "))
if houre_worked <= 40:
    gross_pay = houre_worked * hourly_rate
else:
    overtime_hours = houre_worked - 40 # ลบชั่วโมงทำงานปกติ
    gross_pay = (40 * hourly_rate) + (overtime_hours * hourly_rate * 1.5) # คำนวณเงินเดือนรวมชั่วโมงทำงานปกติและชั่วโมงทำงานล่วงเวลา
print("Your gross pay is:", gross_pay)