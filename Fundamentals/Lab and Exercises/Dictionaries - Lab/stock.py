# After you have completed your first task, your boss decides to give you another one right away. 
# Now not only you have to keep track of the stock, but also you should answer customers if you have some products in stock or not.
# You will be given key-value pairs of products and quantities (on a single line separated by space).
# On the following line, you will be given products to search for. Check for each product. You have 2 possibilities:
# •	If you have the product, print "We have {quantity} of {product} left".
# •	Otherwise, print "Sorry, we don't have {product}".


products = input().split()

stock = {}

for i in range(0, len(products), 2):
    key = products[i]
    value = products[i + 1]
    stock[key] = value

searched = input().split()

for el in searched:
    if el in stock:
        print(f"We have {stock[el]} of {el} left")
    else:
        print(f"Sorry, we don't have {el}")
