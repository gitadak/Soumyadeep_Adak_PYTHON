x=input("Enter the string: ")
x=''.join(sorted(x))
print(x)
x=list(x)
y=list(set(x))
c=[]
for i in range(len(y)):
    c.append(x.count(y[i]))
    print((y[i],c[i]))

