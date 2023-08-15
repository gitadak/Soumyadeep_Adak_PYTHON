import math
try:
    lb=int(input("Enter the lower limit: "))
    ub=int(input("Enter the upper limit: "))
except ValueError:
    print("Invalid input")
    raise SystemExit
if lb<=0 or ub<=0:
    raise Exception("Give positive input")
if lb>ub:
    raise Exception("Lower limit is always less than upper limit")
print("List of primes between %d and %d:"%(lb,ub))
for n in range(lb,ub+1):
    m=0
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            m=1
    if m==0:
        print(n)
