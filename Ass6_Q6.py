x=[]
y=[]
m=int(input("Enter the no. of elements in lists: "))
print("Enter the elements of list1:")
for i in range(m):
    a=input()
    x.append(a)
print("Enter the elements of list2:")
for i in range(m):
    a=input()
    y.append(a)
print("List1:")
print(x)
print("List2:")
print(y)
x=list(set(x))
y=list(set(y))
count=0
for i in x:
    for j in y:
        if i==j:
            count+=1
if count==m:
    print("Containing same elements")
else:
    print("Not same")
