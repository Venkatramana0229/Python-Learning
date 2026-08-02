name = input("Enter your name ")
age = int(input("Enter your age "))

if(age<24):
    clg = input("University name? ")
    print(f"Hi {name} you are {age} years old and a student in {clg}")
else:
    job = input("What do you do for living ")
    print(f"Hi {name} you are {age} years old and {job}")
