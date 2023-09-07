table1=[[1,2,3],[4,5,6]]
print("Values in table1 by row are:")
for row in table1:
    for item in row:
        print("%3d"%item,end="")
    print()