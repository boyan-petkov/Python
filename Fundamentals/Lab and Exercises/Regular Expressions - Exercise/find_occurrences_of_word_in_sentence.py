# Write a program that finds how many times a word is used in a string. 
# The output is a single number indicating the number of times the string contains the word.
# Note that letter case does not matter – it is case-insensitive.

# Input:
# How do you plan on achieving that? How? How can you even think of that? how
# Output:
# 3

import re

string = input()

searched = input()

expression = fr"\b{searched}\b"

matches = re.findall(expression, string, flags=re.I)

print(len(matches))
