# Using a dictionary comprehension, write a program that receives country names on the first line, 
# separated by comma and space ", ", and their corresponding capital cities on the second line (again separated by comma and space ", "). 
# Print each country with their capital on a separate line in the following format: "{country} -> {capital}".

def capital_final():
    country = input().split(", ")
    capitals = input().split(", ")

    final = dict(zip(country, capitals))

    for coun, cap in final.items():
        print(f"{coun} -> {cap}")


capital_final()
