class Employee(object):
    def __init__(self):
        self.name = 'Peter'
        self._age = 45         
        self.__salary = 35000   

 
    def get_salary(self):
        return self.__salary


    def set_salary(self, salary):
        if salary > 0:  # ตรวจสอบไม่ให้เงินเดือนติดลบ
            self.__salary = salary
        else:
            print("Invalid salary amount!")


# สร้าง object
object1 = Employee()

# เข้าถึง attributes
print("Name:", object1.name)
print("Age:", object1._age)

# เข้าถึง private attribute ผ่าน getter
print("Salary:", object1.get_salary())

# เปลี่ยนค่า private attribute ผ่าน setter
object1.set_salary(40000)
print("Updated Salary:", object1.get_salary())
