# example of error handling in python with user input
import Function as f
try:
    a=int(input("Enter the first number: "))
    b=int(input("Enter the second number: "))
    res=a/b
    print(res)
    
    print(f.example(a,b))
    
    
except ZeroDivisionError:
    print("Division by zero is not allowed")