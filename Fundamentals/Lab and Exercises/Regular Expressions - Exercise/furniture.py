# Write a program that calculates the total cost of bought furniture.
# You will be given information about each purchase on separate lines until you receive the command "Purchase". 
# Valid information should be in the format: ">>{furniture_name}<<{price}!{quantity}". 
#   The price could be a floating-point or integer number. You should store the names of the furniture and the total price. 
# In the end, print the name of each bought furniture and the total cost, formatted to the second decimal point:
# "Bought furniture:
# {1st name}
# {2nd name}
# …
# {N name}
# Total money spend: {total_cost}"

# Input:
# >>Sofa<<312.23!3
# >>TV<<300!5
# >Invalid<<!5
# Purchase
# Output:
# Bought furniture:
# Sofa
# TV
# Total money spend: 2436.69

import re

furniture = list()

expression = r">>([a-zA-Z]+)<<(\d+|\d+\.\d+)!(\d+)"
total = 0
command = input()

while not command == "Purchase":
    matches = re.search(expression, command)
    if matches:
        name, price, quantity = matches.groups()
        furniture.append(name)
        total += float(price) * int(quantity)
    command = input()

print("Bought furniture:")
for el in furniture:
    print(f"{el}")
print(f"Total money spend: {total:.2f}")
