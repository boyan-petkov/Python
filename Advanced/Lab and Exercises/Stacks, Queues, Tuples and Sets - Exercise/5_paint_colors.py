# You will have to find all possible color combinations that can be used.
# Write a program that finds colors in a string. You will be given a string on a single line containing substrings (separated by a single space) 
# from which you will be able to form the following colors: 
# Main colors: "red", "yellow", "blue"
# Secondary colors: "orange", "purple", "green"
# To form a color, you should concatenate the first and the last substrings and check if you can get any of the above colors' names. 
# If there is only one substring left, you should use it to do the same check.
# You can only keep a secondary color if the two main colors needed for its creation could be formed from the given substrings:
# •	orange = red + yellow
# •	purple = red + blue
# •	green = yellow + blue
# Note: You could find some of the main colors needed to keep a secondary color after it is found. 
# When you form a color, remove both substrings. Otherwise, you should remove the last character of each substring and 
# return them in the middle of the original string. If the string contains an odd number of substrings, you should put the substrings one position ahead.
# For example, if you are given the string "re yellow bye" you could not form a color with the substring "re" and "bye", 
# so you should remove the last character and return them in the middle of the string: "r by yellow".
# In the end, print out the list with colors in the order in which they are found.

# Input

# •	Single line string

# Output

# •	The list with the collected colors

# Constrains

# •	You will not receive an empty string
# •	Please consider only the colors mentioned above
# •	There won't be any cases with repeating colors

from collections import deque

materials = [int(x) for x in input().split()]
magic_levels = deque([int(x) for x in input().split()])

presents = {
    150: ["Doll", 0],
    250: ["Wooden train", 0],
    300: ["Teddy bear", 0],
    400: ["Bicycle", 0],
}
crafted = set()
while materials and magic_levels:
    material = materials.pop()
    magic = magic_levels.popleft()
    current = material * magic
    if current in presents:
        presents[current][1] += 1
        crafted.add(presents[current][0])

    else:
        if current < 0:
            current = material + magic
            materials.append(current)
        elif current > 0:
            current = material + 15
            materials.append(current)
        elif material == 0 or magic == 0:
            if material == 0 and magic == 0:
                continue
            if material == 0:
                magic_levels.appendleft(magic)
            elif magic == 0:
                materials.append(material)

if ("Doll" in crafted and "Wooden train" in crafted) or ("Teddy bear" in crafted and "Bicycle" in crafted):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")
if materials:
    print(f"Materials left:", ', '.join([str(x) for x in reversed(materials)]))
if magic_levels:
    print(f"Magic left:", ', '.join([str(x) for x in (magic_levels)]))

for value in sorted(presents.values()):
    name, n = value[0], value[1]
    if n > 0:

        print(f"{name}: {n}")
