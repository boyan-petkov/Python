# Using a nested list comprehension, write a program that reads rows of a square matrix and its elements, separated by a comma and a space ", ".
# You should find the matrix's diagonals, prints them and their sum in the format:
# "Primary diagonal: {element1}, {element2}, … {elementN}. Sum: {sum_of_primary}
# Secondary diagonal: {element1}, {element2}, … {elementN}. Sum: {sum_of_secondary}".

rows = int(input())

matrix = []

for _ in range(rows):
    nums = [int(el) for el in input().split(", ")]
    matrix.append(nums)

primary = []
secondary = []

for i in range(rows):
    current = matrix[i][i]
    primary.append(current)
    current2 = matrix[i][rows - 1 - i]
    secondary.append(current2)
total = sum(primary)
total2 = sum(secondary)

print(f"Primary diagonal:", ', '.join([str(x) for x in primary]) + f". Sum: {total}")
print(f"Secondary diagonal:", ', '.join([str(x) for x in secondary]) + f". Sum: {total2}")
