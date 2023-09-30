#Factorial  nPr   nCr
def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)
    
def nPr(n,r):
    return fact(n)//fact(n-r)

def nCr(n,r):
    return nPr(n,r)//fact(r)

'''n=int(input("Enter the value of n: "))
r=int(input("Enter the value of r: "))
print("%d! ="%n,fact(n))
print("%dP%d ="%(n,r),nPr(n,r))
print("%dC%d ="%(n,r),nCr(n,r))'''