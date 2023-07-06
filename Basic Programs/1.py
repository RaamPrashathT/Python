# 1.Write a Python program to solve the equation z = |x  y| * (x + y). #

x=int(input("Enter the value of x:"))
y=int(input("Enter the value of y:"))
z=(abs(x-y))* (x + y)
print("The answer is:",z)
