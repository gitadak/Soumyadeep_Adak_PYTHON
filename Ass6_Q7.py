x=input("Enter the string: ")
x=list(x)
y=list(set(x))
c=[]

for i in range(65,91):
    r=[]
    if chr(i) in y:
        r.extend([chr(i),x.count(chr(i))])
        c.append(r)
    r=[]
    if chr(i+32) in y:
        r.extend([chr(i+32),x.count(chr(i+32))])
        c.append(r)
        
print("Frequency:")
for i in range(len(c)):
    print(c[i][0],"---->",c[i][1])
