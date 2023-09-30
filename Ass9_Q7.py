#Calculate number of local variables declared in a function using function

def fun():
    a, b, c = 1, 2.25, 333
    str = 'GeeksForGeeks'
  
print("Number of Local variables:",fun.__code__.co_nlocals)