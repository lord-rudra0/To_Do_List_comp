
# a =int (input("Enter the number of elements: "))
# i=0
# while i<=10:
#     print(i)
#     i=i+1
    


# # for loop
# for i in range(0,10):
#     n=int(input("Enter the number of elements: "))
#     print(n)


# nested loop


# for i in range(0,2):
#     for j in range(0,2):
#         print(i,j)
#         print("hello")



# # 2d list by user input using nested loop also ask the no of rows and columns and looks like matrices
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

a = []

for i in range(rows):
    row = []
    for j in range(cols):
        element = int(input(f"Enter element for position ({i},{j}): "))
        row.append(element)
    a.append(row)

print("The 2D list is:")
for row in a:
    print(row)






# a=[]
# for i in range(0,2):
#     b=[]
#     for j in range(0,2):
#         n=int(input("Enter the number of elements: "))
        
#         b.append(n)
#     a.append(b)
# print(a)


