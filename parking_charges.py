hours = int(input("Enter parking hours: "))

if hours <= 2:
    charge = 20
elif hours <= 5:
    charge = 50
else:
    charge = 100

print("Parking Charge =", charge)