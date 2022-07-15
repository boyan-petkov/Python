# Write a program that reads from the console a sequence of N usernames and keeps a collection only of the unique ones. 
# On the first line, you will receive an integer N. On the next N lines, you will receive a username. 
# Print the collection on the console (the order does not matter):

usernames_number = int(input())

unique = set()

for _ in range(usernames_number):
    name = input()
    unique.add(name)

print("\n".join(unique))
