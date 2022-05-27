# You want to go to France by train, and the train ticket costs exactly 150$. You do not have enough money, 
# so you decide to buy some items with your budget and then sell them at a higher price – with a 40% markup.
# You will receive a collection of items and a budget in the following format:
# {type->price|type->price|type->price……|type->price}
# {budget}
# The prices for each of the types cannot exceed a specific price, which is given below:
# Type	Maximum Price
# Clothes	50.00
# Shoes	35.00
# Accessories	20.50
# If a price for a particular item is higher than the maximum price, don't buy it. Every time you buy an item, you have to reduce the budget with its price value. 
# If you don't have enough money for it, you can't buy it. Buy as many items as you can.
# Next, you should increase the price of each item you have successfully bought by 40% and then sell it. 
# Calculate if the budget after selling all the items is enough for buying the train ticket.

items = input().split("|")
budget = int(input())
output_list = []
total_spend = 0
total_gained = 0
start_budget = budget

for item in items:
    current_item = item.split("->")
    type = current_item[0]
    price = float(current_item[1])
    buy_now = False
    if budget < price:
        continue

    if "Clothes" in type and price <= 50.00:
        buy_now = True
    elif "Shoes" in type and price <= 35.00:
        buy_now = True
    elif "Accessories" in type and price <= 20.50:
        buy_now = True

    if buy_now:
        budget -= price
        total_spend += price
        sell_price = price + price * 0.40
        total_gained += sell_price
        output_list.append(sell_price)

profit = (total_gained + budget) - start_budget
for element in output_list:
    print(f"{element:.2f}", end=" ")
print()

print(f"Profit: {profit:.2f}")
if total_gained + budget >= 150:
    print(f"Hello, France!")
else:
    print("Not enough money.")
