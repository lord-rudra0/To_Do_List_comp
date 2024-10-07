# tupels by user input

a=[]
n=int(input("Enter the number of elements: "))
for i in range(0,n):
    element=input("Enter element: ")
    a.append(element)
print(a)
print(tuple(a))
print(a[0])
