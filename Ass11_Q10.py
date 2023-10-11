f1=open("file1.txt","r")
f2=open("file2.txt","w")
for contents in f1:
    f2.write(contents.swapcase())
f1.close()
f2.close()
