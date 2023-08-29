s=input("Enter the string: ")
a=s.split()
a.reverse()
s=''
for i in a:
    s=s+i+' '
print("New string:",s)
