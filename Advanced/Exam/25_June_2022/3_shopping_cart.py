# Peter has decided to invite some guests. He should go shopping, but he will need help because 
# there are too many things he needs to remember. Would you assist him?
# Write a function called shopping_cart that adds products to a shopping cart for the following three types of meals:  
#   "Soup", "Pizza", and "Dessert". Every meal has a limit of products that can be added to it:
# •	Soup: 3
# •	Pizza: 4
# •	Dessert: 2
# Once you reach the limit of a meal, you should stop adding products to that meal.
# The function will receive a different number of arguments. The arguments will be passed as tuples with two elements - the first one is the type of meal,
# and the second is the product for the meal. You need to take each argument and make a dictionary with the meal's name as a key and the products as a value of the corresponding key.
# There are some additional requirements:
# •	If you receive the same product for the same meal more than once, you must not add it again.
# •	If you run into the word "Stop" (not tuple) as an argument, you must immediately stop adding products to the cart - just sort and return the desired result as described below.
# In the end, sort the meals by the number of bought products in descending order. 
# If there are meals with an equal number of products, sort them (the meals) by their name in ascending order (alphabetically). 
# For each meal sort its products in ascending order (alphabetically).
# Return an output as described below.
# Note: Submit only the function in the judge system
# Input
# •	There will be no input, just parameters passed to your function
# Output
# •	Return a string for each of the 3 types of a meal of the sorted result in the format:
# o	"{meal_type}:"
# " - {first_product_added}"
# " - {second_product_added}"
#  …
# " - {Nth_product_added}"
# o	If there are no products given for a meal, return just its name in the format shown above.
# •	If there are NO products in the cart (at all), return the message: "No products in the cart!"
# Constrains
# •	Each tuple given will always contain the type of meal in the first position and a product in the second.
# •	There will be no other meals passed than "Soup", "Pizza", and "Dessert".

def shopping_cart(*args):
    pizza_limit = 4
    soup_limit = 3
    dessert_limit = 2
    all_meals_dict = {"Pizza": [], "Dessert": [], "Soup": []}
    for element in args:
        if element == "Stop":
            break
        meal, product = element[0], element[1]
        if product in all_meals_dict[meal]:
            continue
        if meal == "Pizza" and len(all_meals_dict[meal]) == pizza_limit:
            continue
        if meal == "Soup" and len(all_meals_dict[meal]) == soup_limit:
            continue
        if meal == "Dessert" and len(all_meals_dict[meal]) == dessert_limit:
            continue

        all_meals_dict[meal].append(product)

    for meal, products in all_meals_dict.items():
        products = sorted(products)
        all_meals_dict[meal] = products

    sorted_meals = sorted(all_meals_dict.items(), key=lambda x: (-len(x[1]), x[0]))
    result = ""
    if len(all_meals_dict["Pizza"]) == 0 and len(all_meals_dict["Soup"]) == 0 and len(all_meals_dict["Dessert"]) == 0:
        return "No products in the cart!"
    for tuple in sorted_meals:
        name = tuple[0]
        products = tuple[1]
        result += f"{name}:\n"
        if not products:
            continue
        for product in products:
            result += f" - {product}\n"
    return result


