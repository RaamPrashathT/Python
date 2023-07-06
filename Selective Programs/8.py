name=input("Enter your name:")
age=int(input("Enter age:"))
g=input("Enter your gender:")
if(g==m or g==M or g==f or g==F):
    if(age>=18 and age<30 and (g==m or g==M)):
        print("Your wage is 700 per day")
    elif(age>=18 and age<30 and (g==f or g==F)):
        print("Your wage is 750 per day")
    elif(age>=30 and age<=40 and (g==m or g==M)):
        print("Your wage is 800 per day")
    elif(age>=30 and age<=40 and (g==f or g==F)):
        print("Your wage is 800 per day")
else:
    print("please enter a valid gender code")
        
