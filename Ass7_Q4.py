t=[5,'abc',56,(7,'pnb'),98]
count=0
for i in t:
    if type(i)==tuple:
        break
    else:
        count+=1
print(t)
print("No. of elements before",i,"is",count)

