def findSqrt(x):
  if x < 2:
    return x
  y = x
  z = (y + (x/y)) / 2
  while abs(y - z) >= 0.00001: #upto 5 decimal digits
    y = z
    z = (y + (x/y)) / 2
  return z

n=int(input("Enter the number: "))
print("Square root of %d is %.5f"%(n,findSqrt(n)))
