n=int(input("Enter the number: "))
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
    print(n,"is armstrong number")
else:
    print(n,"is not armstrong number")
