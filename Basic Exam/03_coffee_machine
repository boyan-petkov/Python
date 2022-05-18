product_type = input()
sugar = input()
number = int(input())

price = 0
espresso = 0.90
espresso_normal = 1
espresso_sugar = 1.20
cappuccino = 1
cappuccino_normal = 1.20
cappuccino_sugar = 1.60
tea = 0.50
tea_normal = 0.60
tea_sugar = 0.70

if product_type == "Espresso":
    if sugar == "Without":
        price = espresso * number * 0.65
    elif sugar == "Normal":
        price = espresso_normal * number
    else:
        price = espresso_sugar * number
    if number >= 5:
        price *= 0.75
elif product_type == "Cappuccino":
    if sugar == "Without":
        price = cappuccino * number * 0.65
    elif sugar == "Normal":
        price = cappuccino_normal * number
    else:
        price = cappuccino_sugar * number
else:
    if sugar == "Without":
        price = tea * number * 0.65
    elif sugar == "Normal":
        price = tea_normal * number
    else:
        price = tea_sugar * number
if price < 15:
    print(f"You bought {number} cups of {product_type} for {price:.2f} lv.")
else:
    price *= 0.80
    print(f"You bought {number} cups of {product_type} for {price:.2f} lv.")
