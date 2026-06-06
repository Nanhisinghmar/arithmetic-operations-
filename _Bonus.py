salary = int(input("Enter salary: "))

if salary >= 50000:
    bonus = salary * 20 / 100
elif salary >= 30000:
    bonus = salary * 10 / 100
else:
    bonus = salary * 5 / 100

print("Bonus =", bonus)
print("Total Salary =", salary + bonus)