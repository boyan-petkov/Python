# Write a program that receives a matrix and prints the flattened version of it (a list with all the values). 
# For example, the flattened list of the matrix: [[1, 2], [3, 4]] will be [1, 2, 3, 4].
# On the first line, you will receive the number of a matrix's rows. 
# On the next rows, you will get the elements for each column separated with a comma and a space ", ".

n_rows = int(input())

matrix = []
final = []
for _ in range(n_rows):
    nums = [int(el) for el in input().split(", ")]
    matrix.extend(nums)
print(matrix)
