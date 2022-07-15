# Write a program that reads a text from the console and counts the occurrences of each character in it. 
# Print the results in alphabetical (lexicographical) order.  


text = input()

symbols = dict()

for char in text:
    if char not in symbols:
        symbols[char] = 0
    symbols[char] += 1

for kvp in sorted(symbols.items()):
    char, times = kvp[0], kvp[1]
    print(f"{char}: {times} time/s")
