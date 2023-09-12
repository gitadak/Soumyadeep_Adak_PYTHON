queue=[]
rev=[]
n=int(input("Total no. of elements in Queue: "))
while True:
    ch=int(input("1. Enqueue\n2. Dequeue\n3. Exit\nEnter your choice: "))
    if ch==3:
        break
    elif ch==1:
        element=input("Enter the element: ")
        if len(queue)==n:
            print("Queue full")
        else:
            queue.append(element)
        print("Queue:")
        for i in range(len(queue)-1,-1,-1):
            print(queue[i])
    elif ch==2:
        try:
            queue.reverse()
            elm=queue.pop()
            print("Deleted element:")
            print(elm)
            queue.reverse()
            print("Queue:")
            if len(queue)==0:
                print("Empty Queue")
            else:
                for i in range(len(queue)-1,-1,-1):
                    print(queue[i])
        except IndexError:
            print("Empty Queue")
    else:
        print("Invalid Input")
