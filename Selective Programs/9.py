food_rating = int(input("Food Rating (1-5): "))
service_rating = int(input("Service Rating (1-5): "))
ambience_rating = int(input("Ambience Rating (1-5): "))
bill_amount = float(input("Bill Amount: "))
if food_rating >= 4 and service_rating >= 4 and ambience_rating >= 4:
    tip_amount = bill_amount * 0.1  
elif food_rating <= 3 and service_rating <= 3 and ambience_rating <= 3:
    tip_amount = bill_amount * 0.01 
else:
    tip_amount = bill_amount * 0.05
print("Tip Amount: Rs", tip_amount)
