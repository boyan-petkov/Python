# You will be given a sequence of strings, each on a new line until you receive the "stop" command. 
# Every odd line on the console represents a resource (e.g., Gold, Silver, Copper, and so on) and every even - quantity.
# Your task is to collect the resources and print them each on a new line.
# Print the resources and their quantities in the following format:
# "{resource} -> {quantity}"
# The quantities will be in the range [1 … 2 000 000 000].

resources = dict()

command = input()

while not command == "stop":
    current_resource = int(input())
    if command in resources:
        resources[command] += current_resource
    else:
        resources[command] = current_resource
    command = input()

for res, quan in resources.items():
    print(f"{res} -> {quan}")
