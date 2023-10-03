t=(2,8,9,6,3,1,7)
print("Linear search:")
elm=int(input("Enter the element to be found: "))
flag=0
for i in range(len(t)):
    if t[i]==elm:
        flag=1
        print("Found at position",i+1)
        break
if flag==0:
    print("Not found")


t=(2,3,9,10,12)
print("Binary search:")
elm=int(input("Enter the element to be found: "))
flag=0
low=0
high=len(t)-1
while low<=high:
    mid=(low+high)//2
    if t[mid]==elm:
        flag=1
        print("Found at position",mid+1)
        break
    elif elm<t[mid]:
        high=mid-1
    else:
        low=mid+1
if flag==0:
    print("Not found")
