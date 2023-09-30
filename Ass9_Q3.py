#LCM of n numbers
def LCMofTwoNumbers(a,b):
    c=a
    i=2
    while c%b!=0:
        c=a*i
        i+=1
    return c

def LCMofnNumbers(m):
    LCM=LCMofTwoNumbers(m[0],m[1])
    for i in range(2,len(m)):
        LCM=LCMofTwoNumbers(LCM,m[i])
    return LCM

n=int(input("Enter the no. of elements: "))
l=[]
print("Enter the numbers:")
for i in range(n):
    x = int(input())
    l.append(x)
print("LCM = ",LCMofnNumbers(l))
