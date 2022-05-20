# It is time to get in a Christmas mood. You need to decorate the house in time for the big event, 
# but you have limited days to do so.
# Write a program that calculates how much money you will need to spend on Christmas decorations and 
# how much your Christmas spirit will improve.
# On the first line, you will receive the quantity of decorations you should buy each time you go shopping. 
# On the second line, you will receive the days left until Christmas. 
# There are 4 types of decorations, and each piece costs a certain price. 
# Also, each time you go shopping for a concrete type of decoration, your Christmas spirit is improved by some points:
# Decoration	Price/Piece	Points/Shopping
# Ornament Set	2$	5
# Tree Skirt	5$	3
# Tree Garland	3$	10
# Tree Lights	15$	17
# Until Christmas, you go shopping for a certain decoration as follows:
# •	Every second day you buy Ornament Sets.
# •	Every third day you buy Tree Skirts and Tree Garlands.
# •	Every fifth day you buy Tree Lights. 
# o	If you have bought Tree Skirts and Tree Garlands on the same day, you additionally increase your spirit by 30.
# That's not all! You have a cat at home that really likes to mess around with the decoration:
# •	Every tenth day your cat ruins all tree decorations, and you lose 20 points of the spirit:
# o	Because of that, you go shopping (for a second time during the day) to buy one piece of tree skirt, garlands, 
# and lights, but you do NOT earn additional spirit points for them.
# •	Also, because of the cat - at the beginning of every eleventh day, 
# you are forced to increase the quantity of decorations needed to be bought each time you go shopping by 2.
# •	If the last day is a tenth day, the cat demolishes even more and ruins the Christmas turkey, 
# and you lose an additional 30 points of spirit.
# In the end, you must print the total cost and the gained spirit.
# Input / Constraints
# The input will consist of exactly 2 lines:
# •	quantity - integer in the range [1…100]
# •	days - integer in the range [1…100]
# Output
# In the end, print the total cost and the total gained spirit in the following format:
# •	"Total cost: {budget}"
# •	"Total spirit: {totalSpirit}"
quantity = int(input())
days_left = int(input())

ornaments = 2
skirt = 5
garlands = 3
lights = 15
days_counter = 1
spirit = 0
price = 0
condition = False
last_day = days_left
while days_left > 0:
    condition = False
    if days_counter % 11 == 0:
        quantity += 2
    if days_counter % 2 == 0:
        price += ornaments * quantity
        spirit += 5
    if days_counter % 3 == 0:
        price += skirt * quantity + garlands * quantity
        spirit += 13
        condition = True
    if days_counter % 5 == 0:
        price += lights * quantity
        spirit += 17
        if condition:
            spirit += 30
    if days_counter % 10 == 0:
        spirit -= 20
        price += (lights + garlands + skirt)
    days_left -= 1
    days_counter += 1
if last_day % 10 == 0:
    spirit -= 30

print(f"Total cost: {price}")
print(f"Total spirit: {spirit}")




