#Because I cannot include every single submission I get, I will choose one or two 
#that are example answers and include those within each post.
#Create a program that asks the user to enter their name and their age. 
# Print out a message addressed to them that tells them the year that they will turn 
# 100 years old.

name = input("Enter your name: ")
age = int(input("Enter your age: "))
year = str((2023 - age) + 100)
print("Hello " + name + ", you will turn 100 years old in the year " + year + ".")