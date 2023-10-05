from math import sqrt
try:
    num=int(input("Enter the number: "))
    sqroot=sqrt(num)
    print("Square root of",num,"is",sqroot)
except ValueError:
    print("Input must be an positive integer")