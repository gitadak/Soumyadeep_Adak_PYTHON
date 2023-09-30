#Pascal's triangle not using nCr
def PascalNotUsingnCr(n):
    for i in range(1, n+1):
        for j in range(0, n-i):
            print('  ', end='')
        C = 1
        for j in range(1, i+1):
            print("%-4d"%C, end='')
            C = C * (i - j) // j
        print()
    return

n=int(input("Enter the number of rows: "))
PascalNotUsingnCr(n)