#Pascal's triangle of n rows using nCr
from Ass9_Q5 import nCr
def PascalUsingnCr(n):
    for i in range(n):
        for k in range(1,n-i):
            print("  ",end='')
        for j in range(0,i+1):
            print("%-4d"%nCr(i,j),end='')
        print()
    return

n=int(input("Enter the number of rows: "))
PascalUsingnCr(n)