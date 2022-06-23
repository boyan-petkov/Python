# Write a program that counts all characters in a string except for space (" "). 
# Print all the occurrences in the following format:
# "{char} -> {occurrences}"

sentence = input()

dictionary = dict()

for chr in sentence:
    if chr not in dictionary and chr != " ":
        dictionary[chr] = 1
    else:
        if chr != " ":
            dictionary[chr] += 1

for (key, value) in dictionary.items():
    print(f"{key} -> {value}")
