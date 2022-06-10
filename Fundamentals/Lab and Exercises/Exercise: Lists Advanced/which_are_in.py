# You will be given two sequences of strings, separated by ", ". 
# Print a new list containing only the strings from the first input line, which are substrings of any string in the second input line.

first_string = input().split(", ")
second = input().split(", ")

final = []
for el in first_string:
    for word in second:
        if el in word:
            if el not in final:
                final.append(el)
print(final)
