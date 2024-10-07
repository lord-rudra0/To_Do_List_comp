#array basic operations
# a=[1,2,3,4,5]
# print(a)
# print(a[0])
# print(a[1:3])
# print(a[:])
# print(a[::-1])
# print(a[::2])
# print(a[1::2])
# print(a[1:4:2])
# print(a[1:4])
# print(a[1:4:1])
# print(a[1:4:2])


# List in python input by user string
a=[]
n=int(input("Enter the number of elements: "))
for i in range(0,n):
    element=input("Enter element: ")
    a.append(element)
print(a)


a=[]
n=int(input("Enter the number of elements: "))
for i in range(0,n):
    element=int(input("Enter element: "))
    a.append(element)
print(a)
print(a[0])
print(a[1:3])
print(a[:])
print(a[::-1])

