# Write a program that reads a single string with names separated by comma and space ", ". Sort the names by their length in descending order. 
# If 2 or more names have the same length, sort them in ascending order (alphabetically). Print the resulting list.

names = [words for words in input().split(", ")]

names_ = sorted(names)
names_new = sorted(names_, key=len, reverse=True)
print(names_new)
