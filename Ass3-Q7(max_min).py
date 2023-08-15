#max-min
print("Enter the three numbers:")
a=int(input())
b=int(input())
c=int(input())
max=a
min=a
if b>max:
    max=b
if b<min:
    min=b
if c>max:
    max=c
if c<min:
    min=c
print("Maximum = %d\nMinimum = %d"%(max,min))
