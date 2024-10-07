# def example():
#     print("Hello, World!")
#     while True:
#         try:
#             x = int(input("Please enter a number: "))
#             break
#         except ValueError:
#             print("Oops!  That was no valid number.  Try again...")
#     print("You entered", x)
    
# example()

# a function that takes two arguments and returns their sum by user input 
# def example(a,b):
#     a=int(input())
    #   b = int(input())
    #     res = a+b
    #     print(res)
        




# def example(a,b):
#     return a+b
#     # print(res)

# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))
# result=example(num1,num2)
# print(result)


# def fact(n):
#     if n==0:
#         return 1
#     return n*fact(n-1)
# n=int(input("Enter the number: "))  
# result=fact(n)
# print(result)


# def stre(name1,name2):
#     name = name1+" "+name2
#     return name

# a=input("Enter the first name: ")
# b=input("Enter the second name: ")
# result=stre(a,b)
# print(result)


# example of args and kwargs with function in python with user input

# def example(*args):
#     sum1=0
#     for i in args:
#         print(i)
#         sum1+=int(i)
#     print(sum1)
# n=int(input("Enter the number of elements: "))
# a=[]
# for i in range(0,n):
#     element=input("Enter element: ")
#     a.append(element)
# example(*a)


def example(**kwargs):
    for key,value in kwargs.items():
        print(key,value)
n=int(input("Enter the number of elements: "))
a={}
for i in range(0,n):
    key=input("Enter key: ")
    value=input("Enter value: ")
    a[key]=value
example(**a)


