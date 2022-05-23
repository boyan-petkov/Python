# As a gladiator, Peter needs to repair his broken equipment when he loses a fight. His equipment consists of a helmet, a sword, a shield, and an armor. 
# You will receive Peter's lost fights count. 
# Every second lost game, his helmet is broken.
# Every third lost game, his sword is broken.
# When both his sword and helmet are broken in the same lost fight, his shield also breaks.
# Every second time his shield brakes, his armor also needs to be repaired. 
# You will receive the price of each item in his equipment. Calculate his expenses for the year for renewing his equipment. 

lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
shield_counter = 0
repairs = 0

for fight in range(1, lost_fights + 1):
    if fight % 2 == 0:
        repairs += helmet_price
    if fight % 3 == 0:
        repairs += sword_price
    if fight % 2 == 0 and fight % 3 == 0:
        repairs += shield_price
        shield_counter += 1
        if shield_counter % 2 == 0:
            repairs += armor_price
print(f"Gladiator expenses: {repairs:.2f} aureus")
