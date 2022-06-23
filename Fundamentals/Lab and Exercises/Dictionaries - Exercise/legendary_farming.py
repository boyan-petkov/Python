# You are playing a game, and your goal is to win a legendary item - any legendary item will be good enough. 
# However, it's a tedious process, and it requires quite a bit of farming. The possible items are:
# •	"Shadowmourne" - requires 250 Shards
# •	"Valanyr" - requires 250 Fragments
# •	"Dragonwrath" - requires 250 Motes
# "Shards", "Fragments", and "Motes" are the key materials 	(case-insensitive), and everything else is junk. 
# You will be given lines of input in the format: 
# "{quantity1} {material1} {quantity2} {material2} … {quantityN} {materialN}"
# Keep track of the key materials - the first one that reaches 250, wins the race. 
# At that point, you have to print that the corresponding legendary item is obtained. 
# In the end, print the remaining shards, fragments, motes in the format:
# "shards: {number_of_shards}
# fragments: {number_of_fragments}
# motes: {number_of_motes}"
# Finally, print the collected junk items in the order of appearance.

legendary = {"shards": 0, "fragments": 0, "motes": 0}
result = "Shadowmourne", "Valanyr", "Dragonwrath"

goal = False
junk = dict()

while not goal:
    current = input().split()
    for i in range(0, len(current), 2):
        quantity = int(current[i])
        material = current[i + 1].lower()
        if material == "shards" or material == "fragments" or material == "motes":
            legendary[material] += quantity
            if legendary[material] >= 250:
                legendary[material] -= 250
                goal = True
                if material == "shards":
                    print(f"{result[0]} obtained!")
                    break
                elif material == "fragments":
                    print(f"{result[1]} obtained!")
                    break
                elif material == "motes":
                    print(f"{result[2]} obtained!")
                    break
        else:
            if material not in junk:
                junk[material] = quantity
            else:
                junk[material] += quantity
    if goal:
        break
for key, value in legendary.items():
    print(f"{key}: {value}")
for key, value in junk.items():
    print(f"{key}: {value}")
