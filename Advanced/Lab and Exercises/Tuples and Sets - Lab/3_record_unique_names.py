# Write a program, which will take a list of names and print only the unique names in the list.
# The order in which we print the result does not matter.

names_num = int(input())

unique = set()
for _ in range(names_num):
    name = input()
    unique.add(name)

print('\n'.join(unique))
