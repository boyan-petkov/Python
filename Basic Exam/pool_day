from math import ceil

number_of_people = int(input())
entry_tax = float(input())
price_for_sunbed = float(input())
price_for_umbrella = float(input())

entry_price_for_all = number_of_people * entry_tax
sunbed_price = ceil(number_of_people * 0.75) * price_for_sunbed
umbrella_price = ceil(number_of_people / 2) * price_for_umbrella

total = entry_price_for_all + sunbed_price + umbrella_price

print(f"{total:.2f} lv.")
