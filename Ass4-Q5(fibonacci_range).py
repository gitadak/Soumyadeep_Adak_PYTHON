try:
    lb=int(input("Enter the lower limit: "))
    ub=int(input("Enter the upper limit: "))
except ValueError:
    print("Invalid input")
    raise SystemExit
if lb<0 or ub<0:
    raise Exception("Give non-negative input")
if lb>ub:
    raise Exception("Lower limit is always less than upper limit")
print("Fibonacci numbers between %d and %d:"%(lb,ub))
a=0
b=1
c=a+b
if lb==a:
    print (a)
while True:
    if c>ub:
        break
    elif c>=lb:
        print(c)
    a,b=b,c
    c=a+b
