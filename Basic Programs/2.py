'''
2.Write a Python program to calculate the surface volume and area of a cylinder.
  Formula: 
  Volume = pi * radius * radius * height 
  Surface area of a cylinder = ((2*pi*radius)*height) + ((pi*radius**2)*2)
'''


r=int(input("Enter the radius of the cylinder:"))
h=int(input("Enter the height of the cylinder:"))
vol=3.14*r*r*h
SA=((2*3.14*r)*h)+((3.14*r**2)*2)
print("The volume of the cylinderis:",vol)
print("The surface area of the cylinderis:",SA)
