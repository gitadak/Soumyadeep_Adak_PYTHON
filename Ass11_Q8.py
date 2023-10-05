import Ass11_Q2
f1=open("Ass11_Q2_file.txt","r")
f2=open("Ass11_Q8_file.txt","w")
data_f1=f1.read()
data_f2=data_f1[::-1]
f2.write(data_f2)
f1.close()
f2.close()

Ass11_Q2.fread("Ass11_Q8_file.txt")