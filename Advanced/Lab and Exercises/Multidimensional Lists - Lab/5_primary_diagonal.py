# Write a program that finds the sum of all numbers in a matrix's primary diagonal (runs from top left to bottom right). 
# On the first line, you will receive an integer N – the size of a square matrix. 
# The next N lines holds the values for each column - N numbers, separated by a single space. 

rows = int(input())

matrix = []

for _ in range(rows):
    nums = [int(el) for el in input().split()]
    matrix.append(nums)

diagonal = 0

for row_i in range(rows):
    for col_i in range(len(matrix[row_i])):
        if row_i == col_i:
            diagonal += matrix[row_i][col_i]


print(diagonal)
