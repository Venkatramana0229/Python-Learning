from datetime import date

cy = date.today().year
by = int(input("Enter birth year = "))
ymd = date.today()
day = date.today().day


def ogday(day):
     if 11 <= day <= 13:
         return "th"
     return {1: "st", 2: "nd", 3: "rd"}.get(day % 10, "th")
  
  
def ogsuf(current_date):
    suf = ogday(current_date.day)
    return current_date.strftime(f"%B %#d{suf}, %Y")


if(by<cy):
    age = cy-by
    print("Your age is",age)
    print(f"From {by} to {cy} you had gone through alot and you did great, keep going!")
else:
    print("You must be from the future")
    print(f"Because today is {ogsuf(ymd)}")
