try:
    lb=int(input("Enter the lower limit: "))
    ub=int(input("Enter the upper limit: "))
except ValueError:
    print("Invalid input")
    raise SystemExit
if lb>ub:
    raise Exception("Lower limit is always less than upper limit")
if lb<=0 or ub<=0:
    raise Exception("Input must be positive")
print("Armstrong numbers between %d and %d:"%(lb,ub))
for n in range(lb,ub+1):
    s=0
    m=n
    p=n
    count=0
    while p>0:
        count+=1
        p//=10
    while m>0:
        s+=(m%10)**count
        m//=10
    if(n==s):
        print(n)

