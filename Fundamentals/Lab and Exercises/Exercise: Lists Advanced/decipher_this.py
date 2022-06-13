# You are given a secret message you should decipher. To do that, you need to know that in each word:
# •	the second and the last letter are switched (e.g., Holle means Hello)
# •	the first letter is replaced by its character code (e.g., 72 means H)

words = input().split()
final = []

for word in words:
    current = list(word)
    character = [el for el in current if el.isdigit()]
    filtered = [el for el in current if el not in character]
    needed = chr(int("".join(character)))
    filtered.insert(0, needed)
    filtered[1], filtered[-1] = filtered[-1], filtered[1]
    final.append("".join(filtered))

print(" ".join(final))
