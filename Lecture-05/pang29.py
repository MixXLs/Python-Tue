def calculate_stats(numbers):
    total_sum = sum(numbers) # ผลรวมของตัวเลขทั้งหมด
    average = total_sum / len(numbers) # ค่าเฉลี่ย len()นับจำนวนสมาชิกในลิสต์
    maximum = max(numbers) # ค่ามากที่สุด
    minimum = min(numbers) # ค่าน้อยที่สุด
    return total_sum, average, maximum, minimum

numbers = [5, 10, 15, 20, 25]
total, avg, max_num, min_num = calculate_stats(numbers)

print(f"Total Sum: {total}")
print(f"Average: {avg}")
print(f"Maximum: {max_num}")
print(f"Minimum: {min_num}")