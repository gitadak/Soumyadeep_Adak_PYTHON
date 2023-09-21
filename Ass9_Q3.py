n=int(input("Enter the no. of elements: "))
l=[]
print("Enter the numbers:")
for i in range(n):
    x = int(input())
    l.append(x)

def lcm(n1,n2):
    i=1
    while i<=n1 and i<=n2:
        if n1%i==0 and n2%i==0 :
            k=i
        i+=1
    return (n1*n2)//k

LCM=lcm(l[0],l[1])
for i in range(2,len(l)):
    LCM=lcm(LCM,l[i])

print("LCM:",LCM)