# sets input by user

a=set()
n=int(input("Enter the number of elements: "))
for i in range(0,n):
    element=input("Enter element: ")
    a.add(element)
print(a)

a.add("hello")
print(a)

a.remove("hello")
print(a)


b=set()
n=int(input("Enter the number of elements: "))
for i in range(0,n):
    element=input("Enter element: ")
    b.add(element)
print(b)

print(a.union(b))