# Write a program that receives info from the console about people and their phone numbers.
# Each entry should have a name and a number (both strings) separated by a "-". 
# If you receive a name that already exists in the phonebook, update its number.
# After filling the phonebook, you will receive a number – N.
# Your program should be able to perform a search of contact by name and print its details in the format: "{name} -> {number}".
#   In case the contact isn't found, print: "Contact {name} does not exist."

info = input()
contacts = dict()

while not info.isdigit():
    name, num = info.split("-")
    contacts[name] = num
    info = input()

for x in range(int(info)):
    current = input()
    if current in contacts:
        print(f"{current} -> {contacts[current]}")
    else:
        print(f"Contact {current} does not exist.")
