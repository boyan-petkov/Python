# Write a program which keeps track of people who are getting water from a dispenser and the amount of water left at the end. 
# On the first line you will receive the starting quantity of water (integer) in a dispenser. 
# Then, on the next few lines you will be given the names of some people who want to get water (each on separate line) until you receive the command "Start". 
# Add those people in a queue. Finally, you will receive some commands until the command "End":
# -	"{liters}" - litters (integer) that the current person in the queue wants to get. Check if there is enough water in the dispenser for that person.
# o	If there is enough water, print "{person_name} got water" and remove him/her from the queue.
# o	Otherwise, print "{person_name} must wait" and remove the person from the queue without reducing the water in the dispenser.
# -	"refill {liters}" - add the given litters in the dispenser.
# At the end print how many litters of water have left in the format: "{left_liters} liters left".

from collections import deque

liters_in_dispenser = int(input())

command = input()
people = deque()

while not command == "Start":
    people.append(command)
    command = input()

cmd = input()
while not cmd == "End":
    if cmd.startswith("refill"):
        liters_to_fill = cmd.split()[1]
        liters_in_dispenser += int(liters_to_fill)
    else:
        name = people.popleft()
        liters = int(cmd)
        if liters <= liters_in_dispenser:
            print(f"{name} got water")
            liters_in_dispenser -= liters
        else:
            print(f"{name} must wait")
    cmd = input()

print(f"{liters_in_dispenser} liters left")
