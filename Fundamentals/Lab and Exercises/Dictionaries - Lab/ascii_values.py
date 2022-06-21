# Write a program that receives a list of characters separated by ", ". 
# It should create a dictionary with each character as a key and its ASCII value as a value. 
# Try solving that problem using comprehension.


characters = input().split(", ")

final = {chr: ord(chr) for chr in characters}

# for chr in characters:
#     asci = ord(chr)
#     final[chr] = asci

print(final)
