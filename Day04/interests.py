from math import pow

p = float(input("Enter Principal amount = "))
r = float(input("Enter rate of interest = "))
t = float(input("Enter time (in years) = "))

si = (p*r*t)/100
tasi = p + si

taci = p*(pow(1+(r/100),t))
ci = taci - p

print("Simple interest= ",si)
print("Total amount including simple interest = ",tasi)
print("Compound interest= ",ci)
print("Total amount including compound interest = ",taci)
