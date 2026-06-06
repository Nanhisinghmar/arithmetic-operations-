previous = int(input("Enter previous reading: "))
current = int(input("Enter current reading:"))
units = current - previous
if units <= 100:
    bill = units * 2
    print(bill)

elif units <= 200:
    bill = units * 4
    print(bill)

elif units <= 300:
    bill = units * 5 
    print(bill)

else:
    bill = units * 10
    print(bill)

print("Units Consumed =", units)
print("Water Bill =", bill)