'''
3.Write a Python program to calculate the wind chill index.
'''

t=int(input("Enter the temperature in degree celsius:"))
v=int(input("Enter the velocity of the wind in km/h:"))
a=13.12 + 0.6215*t - 11.37*v**0.16 + 0.3965*t*v**0.16
print("The chill indexis:",round(a))
