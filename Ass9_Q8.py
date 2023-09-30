#Recursive function to calculate GCD of a set of given numbers
def GCDofTwoNumbers(a,b):
    if a==b:
        return a
    elif a<b:
        return GCDofTwoNumbers(b,a)
    else:
        return GCDofTwoNumbers(b,a-b)

def GCDofnNumbers(numbers):
    if len(numbers) == 0:
        return None
    elif len(numbers) == 1:
        return numbers[0]
    else:
        current_gcd = GCDofTwoNumbers(numbers[0], numbers[1])
        return GCDofnNumbers([current_gcd] + numbers[2:])

n=int(input("Enter the no. of elements: "))
l=[]
print("Enter the numbers:")
for i in range(n):
    x = int(input())
    l.append(x)
print("GCD = ",GCDofnNumbers(l))
   
