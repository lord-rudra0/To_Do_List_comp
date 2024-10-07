Name=input("Enter the first name: ")
name2=input("Enter the second name: ")
name3=Name+name2
print("The names is", name3)
print(len(name3))

print(name3.upper())
print(name3.lower())

print(name3.replace("a","A"))
print(name3.replace(name3[1:3],"Aman"))

print('ram' in name3) 

print(name3.split(" "))