# Write a program that extracts all elements from a given sequence of words present in it an odd number of times (case-insensitive).
# •	Words are given on a single line, space-separated.
# •	Print the result elements in lowercase, in their order of appearance.


elements = input().split()

initiate = dict()

for el in elements:
    el = el.lower()
    if el not in initiate:
        initiate[el] = 1
    else:
        initiate[el] += 1

for key, value in initiate.items():
    if value % 2 != 0:
        print(key, end=" ")
