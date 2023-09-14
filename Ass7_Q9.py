x={i for i in range(1,11) if i%2!=0}
y=set()
for i in range(1,21):
    count=0
    for j in range(1,i+1):
        if i%j==0:
            count+=1
    if(count==2):
        set1={i}
        y.update(set1)
print(x)
print(y)
print(x&y)#Intersection
print(x|y)#Union
print(x-y)#Difference
print(x^y)#Symmetric difference