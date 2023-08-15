import math
try:
    n=int(input("Enter the number: "))
except ValueError:
    print("Invalid input")
    raise SystemExit
for i in range(2,int(math.sqrt(n))+1):
    if n%i==0:
        print("%d is a composite number"%n)
        raise SystemExit
print("%d is a prime number"%n)
