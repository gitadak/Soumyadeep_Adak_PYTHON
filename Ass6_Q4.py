x=[]
n=int(input("Enter the no. of elements: "))
print("Enter the elements:")
for i in range(n):
    el=int(input())
    x.append(el)
print("List:")
print(x)
print("Frequency of each number:")
y=list(set(x))
for i in y:
    print(i,"->",x.count(i))
