x={i for i in range(1,11) if i%2==0}
y=set()
for i in range(1,21):
    count=0
    for j in range(1,i+1):
        if i%j==0:
            count+=1
    if(count!=2):
        set1={i}
        y.update(set1)
print(x)
print(y)

'''The python all() function accepts an iterable object (such as list,dictionary etc.).
It returns True if all items in passed iterable are true, otherwise it returns False.
If the iterable object is empty, the all() function returns True.'''
print(all(x))
print(all(y))

'''Python Set issuperset() method returns True if all elements of a set B are in set A.
Then Set A is the superset of set B.'''
print(y.issuperset(x))

'''Python set issubset() method returns True if all elements of a set A are present in another set B 
which is passed as an argument, and returns False if all elements are not present in Python.'''
print(y.issubset(x))

print(len(x)) #returns the length of the object

print(sum(x)) #returns the sum of the elements