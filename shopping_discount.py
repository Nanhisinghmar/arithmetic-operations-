amount = int(input("Enter amount: "))
if amount >= 5000:
 #10%discount
    print('final amount=',90/100*amount)
    
#20%discount
elif amount >= 1000:
    print('final amount=' ,80/100*amount)
    
#30%discount
else:
    print('final amount=',70/100*amount)