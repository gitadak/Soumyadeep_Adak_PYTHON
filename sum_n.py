try:
    n=int(input("Enter the no. of terms: "))
except ValueError:
    print("Invalid input")
    raise SystemExit
sum=0
for i in range(1,n+1):
    print(i,"+",end=" ")
    sum+=i
print("\b\b=",sum)
