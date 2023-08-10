list=[]
s=0
while True:
    b=input("Enter number: ")
    if b=='done' and len(list)==0:
        print("No items")
        raise SystemExit
    elif b=='done':
        break
    try:
        a=int(b)
        list.append(a)
        s+=a
    except ValueError:
        print("Invalid input")
list.sort()
print("Maximum = %d\nMinimum = %d\nAverage = %.2f"%(list[-1],list[0],s/len(list)))
