x=[]
y=[]
n=int(input("Enter the no. of elements: "))
print("Enter the elements:")
for i in range(n):
    el=int(input())
    x.append(el)
print("List:")
print(x)
for i in x:
    if i not in y:
        y.append(i)
print("Frequency:")
for i in range(len(y)):
    print(y[i],"->",x.count(y[i]))