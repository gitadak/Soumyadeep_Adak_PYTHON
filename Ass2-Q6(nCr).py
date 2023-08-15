from math import factorial
n=int(input("Enter the value of n: "))
r=int(input("Enter the value of r: "))
ncr=int(factorial(n)/(factorial(r)*factorial(n-r)))
print("nCr =",ncr)
