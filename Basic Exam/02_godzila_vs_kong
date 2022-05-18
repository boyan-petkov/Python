budget_movie = float(input())
number_of_statist = int(input())
price_per_clothe = float(input())

decor_price = budget_movie * 0.10
price_for_clothes = number_of_statist * price_per_clothe
if number_of_statist > 150:
    price_for_clothes = price_for_clothes * 0.90

total_price = decor_price + price_for_clothes
diff = abs(budget_movie - total_price)
if total_price <= budget_movie:
    print("Action!")
    print(f"Wingard starts filming with {diff:.2f} leva left.")
else:
    print("Not enough money!")
    print(f"Wingard needs {diff:.2f} leva more.")
