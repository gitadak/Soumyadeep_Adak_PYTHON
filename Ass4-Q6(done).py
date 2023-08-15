count=0
s=0.0
while True:
    a=input("Enter the number:")
    if a=='done':
        break
    try:
        b=float(a)
        count+=1
        s+=b
    except ValueError as x:
        print(x)
try:
    print("Total = %.2f\nCount = %d\nAverage = %.2f"%(s,count,s/count))
except ZeroDivisionError:
    print("No numbers")
