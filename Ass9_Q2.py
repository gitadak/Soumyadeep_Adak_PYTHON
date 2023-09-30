#Square root of a number using function
def SquareRoot(n):
    return n**0.5

x=int(input("Enter the number: "))
print("Square root of %d = %.5f"%(x,SquareRoot(x)))
