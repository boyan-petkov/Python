
# Aladdin, rich and powerful with the help of the Genie, is now preparing to marry the princess Jasmine. 
# He asks Genie for help to prepare the wedding presents.
# First, you will receive a sequence of integers representing the materials for every wedding present.
# After that, you will be given another sequence of integers – Genie magic level for every aim to make a gift.
# Your task is to mix materials with magic levels so you can make presents, listed in the table below.
# Gift	Magic needed
# Gemstone	100 to 199
# Porcelain Sculpture	200 to 299
# Gold	300 to 399
# Diamond Jewellery	400 to 499
# To make a present, you should take the last integer of materials and sum it with the first magic level value. 
# If the result is between or equal to the numbers described in the table above, you make the corresponding gift and remove both materials and magic value. Otherwise:
# •	If the product of the operation is under 100:
# o	And if it is an even number, double the materials, and triple the magic, then sum it again. 
# o	And if it is an odd number, double the sum of the materials and the magic level. 
# Then, check again if it is between or equal to any of the numbers in the table above.
# •	If the product of the operation is more than 499, divide the sum of the material and the magic level by 2. 
# Then, check again if it is between or equal to any of the numbers in the table above.
# •	If, however, the result is not between or equal to any of the numbers in the table above after performing the calculation, 
# remove both the materials and the magic level.
# Stop crafting gifts when you are out of materials or magic level.
# You have succeeded in crafting the presents when you've crafted either one of the pairs - a gemstone and a sculpture or gold and jewellery.

# Input
# •	The first line of input will represent the values of materials - integers, separated by a single space
# •	On the second line, you will be given the magic levels - integers, separated by a single space

# Output
# •	On the first line - print whether you have succeeded in crafting the presents:
# o	"The wedding presents are made!"
# o	"Aladdin does not have enough wedding presents."
# •	On the next two lines print the materials and magic that are left, if there are any, otherwise skip the line:
# o	"Materials left: {material1}, {material2}, …"
# o	"Magic left: {magicValue1}, {magicValue2}, …
# •	On the next lines, print the gifts alphabetically that the Genie has crafted at least once:
# "{present1}: {amount}
# {present2}: {amount}
# …
# {presentN}: {amount}"
  
# Constraints
# •	All the materials values will be integers in the range [1, 1000]
# •	Magic level values will be integers in the range [1, 1000]


from collections import deque


def requirements_true(current_result,):
    for key_, requirements_ in gifts.items():
        if requirements_[0] <= current_result <= requirements_[1]:
            finished[key_] += 1
            return True
    return False


gifts = {
    "Gemstone": [100, 199],
    "Porcelain Sculpture": [200, 299],
    "Gold": [300, 399],
    "Diamond Jewellery": [400, 499]
}

finished = {}
for name in gifts.keys():
    finished[name] = 0

materials = [int(x) for x in input().split()]
magic_levels = deque([int(x) for x in input().split()])

successful = False

while materials and magic_levels:
    material, level, = materials.pop(), magic_levels.popleft()
    result = material + level
    if result > 499:
        result /= 2
        if requirements_true(result):
            continue

    if requirements_true(result):
        continue


    if result < 100 and result % 2 == 0:
        result = material * 2 + level * 3
        if requirements_true(result):
            continue
    elif result < 100 and result % 2 != 0:
        result *= 2
        if requirements_true(result):
            continue


pair1 = False
pair2 = False

if finished["Gemstone"] > 0 and finished["Porcelain Sculpture"] > 0:
    pair1 = True
if finished["Gold"] > 0 and finished["Diamond Jewellery"] > 0:
    pair2 = True

if pair1 or pair2:
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")

if materials:
    print("Materials left:",", ".join(str(x) for x in materials))
if magic_levels:
    print("Magic left:", ", ".join(str(x) for x in magic_levels))

end_result = {}
for gift_name, times in finished.items():
    if times > 0:
        end_result[gift_name] = times

end_result = dict(sorted(end_result.items(), key = lambda kvp: kvp[0]))
for kvp in end_result.items():
    print(f"{kvp[0]}: {kvp[1]}")
