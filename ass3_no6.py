count=0
s=0
while(True):
    a=input("Enter the number:")
    if a=='done':
        break
    try:
        b=int(a)
        count+=1
        s+=b
    except ValueError:
        print("Invalid input")
try:
    print("Total = %d\nCount = %d\nAverage = %.2f"%(s,count,s/count))
except ZeroDivisionError:
    print("No numbers")