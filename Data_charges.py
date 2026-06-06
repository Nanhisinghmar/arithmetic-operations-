data = int(input("Enter data used (GB): "))

if data <= 2:
    charge = 50
elif data <= 5:
    charge = 100
else:
    charge = 150

print("Data Charge =", charge)