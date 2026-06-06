income = int(input("Enter income: "))

if income <= 250000:
    tax = 0
elif income <= 500000:
    tax = income * 5 / 100
elif income <= 1000000:
    tax = income * 10 / 100
else:
    tax = income * 20 / 100

print("Tax =", tax)