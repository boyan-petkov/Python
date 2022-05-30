# Write a function that calculates the total price of an order and returns it. 
# The function should receive one of the following products: "coffee", "coke", "water", or "snacks", and a quantity of the product. 
#   The prices for a single piece of each product are: 
# •	coffee - 1.50
# •	water - 1.00
# •	coke - 1.40
# •	snacks - 2.00

# Print the result formatted to the second decimal place.


def order(product, number):
    if product == "coffee":
        price = 1.50
        return price * number
    elif product == "coke":
        price = 1.40
        return price * number
    elif product == "water":
        price = 1.00
        return price * number
    elif product == "snacks":
        price = 2.00
        return price * number


current_product, current_number = input(), int(input())
print(f"{order(current_product, current_number):.2f}")
