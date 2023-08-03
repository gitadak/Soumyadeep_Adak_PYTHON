temp1=float(input("Enter the temperature: "))
unit1=input("Enter the unit: ")
if unit1=='C':
    temp2=9*temp1/5.0+32
    unit2='F'
elif unit1=='F':
    temp2=(temp1-32)*5/9.0
    unit2='C'
else:
    print("Invalid input")
    exit(0)
print("Converted temperature: %.2f\nUnit:"%temp2,unit2)
