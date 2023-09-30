#Factors of a number
def factors(n):
    l=[]
    for i in range(1,n//2+1):
        if n%i==0:
            l.append(i)
    return l

n=int(input("Enter the number: "))
m=factors(n)
if len(m)==0:
    print("Input must be greater than 1")
    raise SystemExit
print("Factors of",n)
for i in m:
    print(i)


