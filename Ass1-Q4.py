hour=int(input("enter the working hours: "))
rate=float(input("Enter the hourly rate: "))
if hour>40:
    pay=hour*rate*1.5
else:
    pay=hour*rate
print("Amount to be paid = %.2f"%pay)
