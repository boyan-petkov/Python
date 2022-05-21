# Beaches are filled with sand, water, fish, and sun. Given a string, 
# calculate how many times the words "Sand", "Water", "Fish", and "Sun" appear (case insensitive).

string = input()

string = string.lower()
water = string.count("water")
sun = string.count("sun")
fish = string.count("fish")
sand = string.count("sand")

print(water + sand + sun + fish)
