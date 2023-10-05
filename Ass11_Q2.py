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

def fread(file):
    try:
        f=open(file,"r")
        contents=f.read()
        print(contents)
        f.close()
    except IOError:
        print("File doesnot exist.")
    return

def fread_first_two_lines(file):
    try:
        f=open(file,"r")
        contents=f.readlines()
        for i in range(2):
            print(contents[i])
        f.close()
    except IOError:
        print("File doesnot exist.")
    except IndexError:
        print("Write atleast two lines")
    return

def fread_first_two_chars(file):
    try:
        f=open(file,"r")
        contents=f.read()
        for i in range(5):
            print(contents[i])
        f.close()
    except IOError:
        print("File doesnot exist.")
    except IndexError:
        print("Write atleast 5 characters")
    return

def fread_loop(file):
    try:
        f=open(file,"r")
        for line in f:
            print(line)
        f.close()
    except IOError:
        print("File doesnot exist.")
    return

'''fwrite("Ass11_Q2_file.txt") 
fread("Ass11_Q2_file.txt")
fread_first_two_lines('Ass11_Q2_file.txt')
fread_first_two_chars('Ass11_Q2_file.txt')
fread_loop("Ass11_Q2_file.txt")'''