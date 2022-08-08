
# Write a function called shopping_list which will receive an integer number representing the budget in leva and a different number of keywords. 
# Each key represents the product (string), and each value will be a tuple with the product's price (integer or float number) 
# at the first position and quantity (integer) at the second position.
# Your job is to return which products you bought with the given budget. You only buy a product if you can buy all of its quantity.
# You could only start shopping if you have at least 100 leva budget. 
# Otherwise, you should stop the program and return "You do not have enough budget.".
# Also, you are carrying a basket that cannot hold more than 5 types of products. You should stop buying products:
# •	if you reach the allowed amount of types of products (no matter their quantity)
# •	if you did not reach the allowed amount, but you do not have more products on the shopping list
# You should always buy products successively!
# For each product (all its quantity) you succeeded to buy, return a string on a new line in the following format:
# "You bought {product_name} for {total_price} leva."
# Note: Submit only the function in the judge system
  
# Input
# •	There will be no input, and just parameters passed to your function

# Output
# •	The function should return strings on separate lines containing the bought products and their price in the format described above.
# •	The total price should be formatted to the second decimal point.

def shopping_list(budget: int, **kwargs):
    start_shopping = False
    basket = 0
    products = 0
    print_list = []
    if budget < 100 and start_shopping is False:
        return "You do not have enough budget."

    start_shopping = True

    for product, price_quantity in kwargs.items():
        price, quantity = float(price_quantity[0]), int(price_quantity[1])
        sum_current_product = price * quantity
        if sum_current_product <= budget:
            budget -= sum_current_product
            print_list.append(f"You bought {product} for {sum_current_product:.2f} leva.")
            basket += 1
            products += 1
            if basket == 5 or products == len(kwargs):
                break
    return '\n'.join(print_list)

print(shopping_list(104,
                    cola=(1.20, 2),
                    candies=(0.25, 15),
                    bread=(1.80, 1),
                    pie=(10.50, 5),
                    tomatoes=(4.20, 1),
                    milk=(2.50, 2),
                    juice=(2, 3),
                    eggs=(3, 1),
                    ))

