n=input("Enter your name:")
s=int(input("Enter your salary:"))
y=int(input("Enter number of years of service:"))
if(y>=10):
    print("Your bouns is",s+((s*10)/100))
elif(y<10 and y>=6):
    print("Your bouns is",s+((s*8)/100))
elif(y<6):
    print("Your bouns is",s+((s*5)/100))
