# Write a regular expression to match a valid phone number from Sofia. After you find all valid phones, print them on the console, separated by a comma and a space ", ".
# Compose the Regular Expression
# A valid number has the following characteristics:
# •	It starts with "+359"
# •	Then, it is followed by the area code (always 2)
# •	After that, it is followed by a number:
# o	The number consists of 7 digits (separated into two groups of 3 and 4 digits, respectively). 
# •	The different parts are separated by either a space or a hyphen ('-').
# You can use the following RegEx properties to help with the matching: 
# •	Use quantifiers to match a specific number of digits
# •	Use a capturing group to make sure the delimiter is only one of the allowed characters (space or hyphen) and 
# not a combination of both (e.g., +359 2-111 111 has mixed delimiters, it is invalid). Use a group backreference to achieve this.
# •	Add a word boundary at the end of the match to avoid partial matches.
# •	Ensure that there is a space before the '+' sign, or it is positioned at the beginning of the string.

# Match ALL of these
# +359 2 222 2222
# +359-2-222-2222
# Match NONE of these
# +359 2 222 2222
# +359-2-222-2222	359-2-222-2222, +359/2/222/2222, +359-2 222 2222
# +359 2-222-2222, +359-2-222-222, +359-2-222-22222

import re

numbers = input()

expression = r"\+359([ |-])2\1\d{3}\1\d{4}\b"

matches = re.finditer(expression, numbers)

final = list()
for match in matches:
    # print(match.group()) #you can also specify the group you want
    final.append(match.group())
print(", ".join(final))
