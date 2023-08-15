try:
    n=int(input("Enter the number: "))
    if n<0:
        raise Exception("Input positive number")
    fact=1
    for i in range(n,0,-1):
        fact*=i
    print("%d! = %d"%(n,fact))
except ValueError:
    print("Invalid input")
