def count(file):
    try:
        f=open(file,"r")
        count_line = 0
        count_word = 0
        words=[]
        for line in f:
            count_line+=1
            words=line.split()
            count_word += len(words)
            words=[]
        f.close()
        print("Number of lines:",count_line)
        print("Number of words:",count_word)
    except IOError:
        print("No such file")
    return

count("Ass11_Q2_file.txt")
    