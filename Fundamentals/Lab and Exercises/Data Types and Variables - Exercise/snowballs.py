# Tony and Andi love playing in the snow and having snowball fights, but they always argue about which makes the best snowballs. 
# They have decided to involve you in their fray by writing a program that calculates snowball data and outputs the best snowball value.
# You will receive N – an integer, the number of snowballs being made by Tony and Andi.
# On the following lines, you will receive 3 inputs for each snowball:
# •	The weight of the snowball (integer).
# •	The time needed for the snowball to get to its target (integer).
# •	The quality of the snowball (integer).
# For each snowball, you must calculate its value by the following formula:
# (snowball_weight / snowball_time) ** snowball_quality
# In the end, you must print the highest calculated value of a snowball.

snowballs = int(input())

best_value, best_weight, best_time, best_quality = 0, 0, 0, 0

for snowball in range(snowballs):
    weight = int(input())
    time_needed = int(input())
    quality = int(input())
    current_value = (weight / time_needed) ** quality
    if current_value > best_value:
        best_value = current_value
        best_weight = weight
        best_time = time_needed
        best_quality = quality
print(f"{best_weight} : {best_time} = {best_value:.0f} ({best_quality})")
	
