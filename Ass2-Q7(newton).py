m=float(input("Enter the mass: "))
u=float(input("Enter the initial velocity: "))
v=float(input("Enter the final velocity: "))
t=float(input("Enter the time taken:"))
a=(v-u)/t
F=m*a
s=u*t+.5*a*t**2
print("F=%.2f\na=%.2f\ns=%.2f"%(F,a,s))
