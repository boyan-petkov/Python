# Write a program that takes a single string and prints a list of all the capital letters indices.


text = input()
capitals = []

for index in range (len(text)):
    if text[index].isupper():
        capitals.append(index)
print(capitals)
