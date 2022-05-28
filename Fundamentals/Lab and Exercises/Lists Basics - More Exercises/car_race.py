# Write a program that announces the winner of a car race. 
# You will receive a sequence of numbers. Each number represents the time needed for the car to pass through that step (the index). 
# There will be two cars. The first one starts from the left side, and the other one starts from the right side. 
# The middle index of the sequence is the finish line. 
# Calculate the total time each racer needs to reach the finish line and print the winner with his total time (the racer with less time). 
# If you have a zero in the list, you should reduce the racer's time that reached it by 20% (from his current time).
# The number of elements in the sequence will always be odd.
# Print the result in the following format "The winner is {left/right} with total time: {total_time}".
# The time should be formatted to the first decimal point.

race = [int(i) for i in input().split(' ')]
finish = len(race) // 2
f_car = race[0:finish]
s_car = race[-1:finish:-1]
 
score_f_car = 0
score_s_car = 0
 
for _ in f_car:
    score_f_car += _
    if _ == 0:
        score_f_car *= 0.8
 
 
 
for _ in s_car:
    score_s_car += _
    if _ == 0:
        score_s_car *= 0.8
 
 
if score_f_car > score_s_car:
    print(f"The winner is right with total time: {score_s_car:.1f}")
else:
    print(f"The winner is left with total time: {score_f_car:.1f}")
