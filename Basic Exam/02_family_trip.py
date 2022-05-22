family_budget = float(input())
number_of_nights = int(input())
price_for_night = float(input())
percent_for_additional_cost = int(input()) / 100


if number_of_nights <= 7:
    price_for_all_nights = number_of_nights * price_for_night
else:
    price_for_all_nights = (number_of_nights * price_for_night) * 0.95

budget_after_percent_additional_cost = family_budget - (family_budget * percent_for_additional_cost)

diff = abs(price_for_all_nights - budget_after_percent_additional_cost)
if budget_after_percent_additional_cost >= price_for_all_nights:
    print(f"Ivanovi will be left with {diff:.2f} leva after vacation.")
else:
    print(f"{diff:.2f} leva needed.")
