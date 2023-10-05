def fread(file):
    try:
        f=open(file,"r")
        contents=f.read()
        print(contents)
        f.close()
    except IOError:
        print("File doesnot exist.")
    return

fread("Ass11_Q3_file.txt")
