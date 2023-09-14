t=(3,5,8,9)
print(t)
s=int(input("Enter the element to be found: "))    
try:
    print("Position:",t.index(s))
except ValueError:
    print("Not found")

st=input("Enter the string: ")
t1=tuple(st.split())
print(t1)
m=input("Enter the element to be found: ") 
print("Position:",st.index(m))
print("position:",st.index(m,0))
print("position:",st.index(m,0,-1))