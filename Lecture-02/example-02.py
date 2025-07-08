weight = int(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

#x = height / 100
#bml = weight / (x * x)

bmi = weight / (height * height)

print("Your BMI is", format(bmi, '.2f'))