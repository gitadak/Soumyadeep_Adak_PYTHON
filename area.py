import math
print("Enter the three sides of the triangle:")
a=float(input())
b=float(input())
c=float(input())
if a+b>c and b+c>a and c+a>b:
    s=(a+b+c)/2
    area=math.sqrt(s*(s-a)*(s-b)*(s-c))
    print("Area=%.2f"%area)
else:
    print("Invalid input")
