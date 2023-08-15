#Interest calculation
p=float(input("Enter the principal amount: "))
r=float(input("Enter the annual interest(%): "))
t=int(input("Enter the years: "))
i=p*r*t/100
ta=p+i
print("Total interest: %.2f\nTotal amount: %.2f"%(i,ta))
