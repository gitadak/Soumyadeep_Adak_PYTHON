def LeftRightAngleTriag():
    n=int(input("Enter the number of rows: "))
    for i in range(1,n+1):
        for j in range(1,i+1):
            print("*",end='')
        print()
    return

def RightRightAngleTriag():
    n=int(input("Enter the no. of rows: "))
    for i in range(1,n+1):
        for k in range(1,n+1-i):
            print(" ",end='')
        for j in range(1,i+1):
            print("*",end='')
        print()
    return

def Triag():
    n=int(input("Enter the no. of rows: "))
    for i in range(1,n+1):
        for k in range(1,n+1-i):
            print(" ",end='')
        for j in range(1,i+1):
            print(" *",end='')
        print()
    return

def NaturalNum1():
    n=int(input("Enter the no. of rows: "))
    for i in range(1,n+1):
        for j in range(1,i+1):
            print("%2d"%j,end='')
        print()
    return

def NaturalNum2():
    n=int(input("Enter the no. of rows: "))
    a=1
    for i in range(1,n+1):
        for j in range(1,i+1):
            print("%-3d"%a,end='')
            a+=1
        print()
    return

