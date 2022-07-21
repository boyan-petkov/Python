# Write a program that reads a rectangular matrix's dimensions and finds the 3x3 square with a maximum sum of its elements. 
# There will be no case with two or more 3x3 squares with equal maximal sum.

# Input
# •	On the first line, you will receive the rows and columns in the format "{rows} {columns}" – integers in the range [1, 20]
# •	On the following lines, you will receive each row with its columns - integers, separated by a single space in the range [-20, 20]

# Output
# •	On the first line, print the maximum sum of the elements in the 3x3 square in the format "Sum = {sum}"
# •	On the following 3 lines, print each element of the found submatrix, separated by a single space

from sys import maxsize
rows, columns = [int(el) for el in input().split()]

matrix = []

for _ in range(rows):
    matrix.append([int(el) for el in input().split()])
current_max = -maxsize
best_nums = []
for row_i in range(rows - 2):
    for col_i in range(columns - 2):
        current = [
            matrix[row_i][col_i], matrix[row_i][col_i + 1], matrix[row_i][col_i + 2],
            matrix[row_i + 1][col_i], matrix[row_i + 1][col_i + 1], matrix[row_i + 1][col_i + 2],
            matrix[row_i + 2][col_i], matrix[row_i + 2][col_i + 1], matrix[row_i + 2][col_i + 2]
        ]
        if sum(current) > current_max:
            current_max = sum(current)
            best_nums = current.copy()
print(f"Sum = {current_max}")
print(f"{best_nums[0]} {best_nums[1]} {best_nums[2]}")
print(f"{best_nums[3]} {best_nums[4]} {best_nums[5]}")
print(f"{best_nums[6]} {best_nums[7]} {best_nums[8]}")
