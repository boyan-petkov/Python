# Write a program that keeps the information about products and their prices. Each product has a name, a price, and a quantity:
# •	If the product doesn't exist yet, add it with its starting quantity.
# •	If you receive a product, which already exists, increases its quantity by the input quantity and if its price is different, replace the price as well.
# You will receive products' names, prices, and quantities on new lines. Until you receive the command "buy", keep adding items. 
# Finally, print all items with their names and the total price of each product. 

def multiply(list):
    result = 1
    for x in list:
        result = result * x
    return result


orders = dict()

current = input()
while not current == "buy":
    product, price, (quantity) = current.split()
    if product not in orders:
        orders[product] = []
        orders[product].append(float(price))
        orders[product].append(int(quantity))
    else:
        orders[product][1] += int(quantity)
        if orders[product][0] != (price):
            orders[product][0] = float(price)

    current = input()

for item, value in orders.items():
    print(f"{item} -> {multiply(value):.2f}")
