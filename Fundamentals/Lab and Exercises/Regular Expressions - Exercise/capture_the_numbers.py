# Write a program that receives strings on different lines and extracts only the numbers. 
# Print all extracted numbers on a single line, separated by a single space.

# Input: 
#   The300
#   What is that?
#   I think it's the 3rd movie 
#   Let's watch it at 22:45

# Output:
#   300 3 22 45


import re

lines = []
while True:
    line = input()
    if line:
        lines.append(line)
    else:
        break
text = ' '.join(lines)

expression = r"\d+"

searched = re.findall(expression, text)

final = list()

for el in searched:
    final.append(el)
print(" ".join(final))
