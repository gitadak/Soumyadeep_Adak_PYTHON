stack=[]
n=int(input("Total no. of elements in Stack: "))
while True:
    ch=int(input("1. PUSH\n2. POP\n3. Exit\nEnter your choice: "))
    if ch==3:
        break
    elif ch==1:
        element=input("Enter the element: ")
        if len(stack)==n:
            print("Stack overflow")
        else:
            stack.append(element)
            print("Stack:")
            for i in range(len(stack)-1,-1,-1):
                print(stack[i])
    elif ch==2:
        try:
            elm=stack.pop()
            print("Popped element:")
            print(elm)
            print("Stack:")
            if len(stack)==0:
                print("Empty stack")
            else:
                for i in range(len(stack)-1,-1,-1):
                    print(stack[i])
        except IndexError:
            print("Stack underflow")
    else:
        print("Invalid Input")



