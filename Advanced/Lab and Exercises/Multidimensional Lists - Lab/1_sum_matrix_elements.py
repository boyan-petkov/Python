# Write a program that reads a matrix from the console and prints:
# •	The sum of all numbers in the matrix
# •	The matrix itself
# On the first line, you will receive the matrix sizes in the format "{rows}, {columns}". 
# On the next rows, you will get elements for each column separated by a comma and a space ", ". 

rows, columns = [int(el) for el in input().split(", ")]

matrix = []
total = 0
for row in range(rows):
    nums = [int(el) for el in input().split(", ")]
    total += sum(nums)
    matrix.append(nums)
print(total)
print(matrix)
    
