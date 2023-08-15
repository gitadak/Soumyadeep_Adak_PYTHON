list=[]
try:
    n=int(input("Enter the number of elements: "))
    print("Enter the elements:")
    for i in range(n):
        a=int(input())
        list.append(a)
except ValueError:
    print("Invalid input")
    raise SystemExit
print("The elements:")
for i in list:
    print(i)
print("No more items")
