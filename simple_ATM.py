balance = int(input("Enter Balance: "))
amount = int(input("Enter Amount: "))

if amount <= balance:
    balance = balance - amount
    print("Withdrawal Successful")
    print("Remaining Balance:", balance)
else:
    print("Insufficient Balance")