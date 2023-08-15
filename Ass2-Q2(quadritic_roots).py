import cmath
a=float(input("Enter the coefficient of x^2:"))
b=float(input("Enter the coefficient of x:"))
c=float(input("Enter the constant term:"))
d=b**2-4*a*c
x=((-b)+cmath.sqrt(d))/(2*a)
y=((-b)-cmath.sqrt(d))/(2*a)
print("Roots are--\n",x,'\n',y)
