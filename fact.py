#nCr
import math
n=int(input("Enter the value of n: "))
r=int(input("Enter the value of r: "))
ncr=math.factorial(n)/(math.factorial(r)*math.factorial(n-r))
print("nCr=",int(ncr))
