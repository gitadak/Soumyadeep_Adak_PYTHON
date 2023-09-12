n=int(input("Enter the no. of values: "))
values=[]
for i in range(n):
    newValue=int(input("Enter integer %d:"%(i+1)))
    values.append(newValue)
print("Histogram:")
print("%s %10s %10s"%("Element","Value","Histogram"))
for i in range(len(values)):
    print("%7d %10d  %s"%(i,values[i],"*"*values[i]))
