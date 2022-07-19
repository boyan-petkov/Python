# Write a program that reads a matrix from the console and prints the sum for each column on separate lines. 
# On the first line, you will get matrix sizes in format "{rows}, {columns}". 
# On the next rows, you will get elements for each column separated with a single space. 


rows, column = [int(el) for el in input().split(", ")]

matrix = []

for _ in range(rows):
    nums = [int(el) for el in input().split()]
    matrix.append(nums)

for col_i in range(column):
    current = 0
    for row_i in range(rows):
        current += matrix[row_i][col_i]
    print(current)

