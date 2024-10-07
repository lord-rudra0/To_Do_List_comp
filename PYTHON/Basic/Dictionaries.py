# #dictionaries input by user

# a={}
# n=int(input("Enter the number of elements: "))
# for i in range(0,n):
#     key=input("Enter key: ")
#     value=input("Enter value: ")
#     a[key]=value
# print(a)
# print(a.keys())
# print(a.values())
# print(a.items())    
# print(a.get("name"))
# print(a.get("name1"))
# print(a.get("name1","not found")) #if the key is not found it will print the value in the second argument
# print(a.get("name","not found"))

# key1=input("Enter the key to delete: ")
# if key1 in a:
#    value=a.pop(key1)
# print(a)

#use of nested dictionaries

a={}
n=int (input("Enter the number of elements: "))
for i in range(0,n):
    key=input("Enter key: ")
    value=input("Enter value: ")
    a[key]=value
print(a)

b={}
n=int (input("Enter the number of elements: "))
for i in range(0,n):
    key=input("Enter key: ")
    value=input("Enter value: ")
    b[key]=value
print(b)

c={}
n=int (input("Enter the number of elements: "))
for i in range(0,n):
    key=input("Enter key: ")
    value=input("Enter value: ")
    c[key]=value
print(c)

d={}
d["dict1"]=a
d["dict2"]=b
d["dict3"]=c
print(d)


# c["dict1"]=a
# c["dict2"]=b
# print(c)

# print(c["dict1"])
# print(c["dict2"])
# print(c["dict1"]["name"])