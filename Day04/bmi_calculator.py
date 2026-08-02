import math

w = float(input("Enter weight(kg) = "))
h = float(input("Enter height(m) = "))

bmi = w / (h ** 2)

print("Your BMI is",round(bmi,2))
