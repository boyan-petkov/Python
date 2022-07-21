# Write a program that finds the difference between the sums of the square matrix diagonals (absolute value).
# On the first line, you will receive an integer N - the size of a square matrix. 
# The following N lines hold the values for each column - N numbers separated by a single space. 
# Print the absolute difference between the primary and the secondary diagonal sums.

rows = int(input())

matrix = []

for _ in range(rows):
    nums = [int(el) for el in input().split(" ")]
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

print(abs(total - total2))
