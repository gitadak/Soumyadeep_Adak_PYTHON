import math
a=int(input("Enter the value of a: "))
b=int(input("Enter the value of b: "))
lcm=a*b/math.gcd(a,b)
print("LCM=",int(lcm))
