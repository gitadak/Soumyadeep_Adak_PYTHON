playList=[]
print("Enter your 5 favourite Shakespearean plays:")
for i in range(5):
    playName=input("Play %d:"%(i+1))
    playList.append(playName)
print("Subscript Value:")
for i in range(len(playList)):
    print("%9d%-25s"%(i+1,playList[i]))
