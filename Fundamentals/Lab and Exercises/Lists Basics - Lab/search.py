# On the first line, you will receive a number n. On the second line, you will receive a word. 
# On the following n lines, you will be given some strings. 
# You should add them to a list and print them. 
# After that, you should filter out only the strings that include the given word and print that list too.

number = int(input())

key = input()
non_filter = []
filtered = []
for _ in range(number):
    current = input()
    non_filter.append(current)
    if key in current:
        filtered.append(current)
print(non_filter)
print(filtered)
