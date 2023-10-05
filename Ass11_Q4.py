def fwrite(file):
    try:
        f=open(file,"w")
        while True:
            f.write(input("Write a line: "))
            f.write("\n")
            ch=input("Do u want to write again (y/n): ")
            if ch=='n' or ch=='N':
                break
        f.close()
    except IOError:
        print("File can not be created")
    return

fwrite("Ass11_Q2_file.txt") 