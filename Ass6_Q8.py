stack=[]
while True:
    ch=int(input("1. PUSH\n2. POP\n3. Exit\nEnter your choice: "))
    if ch==3:
        break
    elif ch==1:
        element=input("Enter the element: ")
        stack.append(element)
        print("Stack:")
        for i in range(len(stack)-1,-1,-1):
            print(stack[i])
    else:
        try:
            print("Popped element:")
            print(stack.pop())
            print("Stack:")
            for i in range(len(stack)-1,-1,-1):
                print(stack[i])
        except IndexError:
            print("Stack underflow")


