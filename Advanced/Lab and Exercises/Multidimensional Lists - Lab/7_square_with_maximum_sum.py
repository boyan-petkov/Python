# Write a program that reads a matrix from the console and finds the 2x2 top-left submatrix with biggest sum of its values. 
# On first line you will get matrix sizes in format "{rows}, {columns}". 
# On the next rows, you will get elements for each column, separated with a comma and a space ", ". 
# You should print the found submatrix and the sum of its elements as shown in the examples. 

rows, columns = [int(el) for el in input().split(", ")]

matrix = []

for _ in range(rows):
    nums = [int(el) for el in input().split(", ")]
    matrix.append(nums)
biggest = 0
digits = []
for row_i in range(rows - 1):
    for col_i in range(columns - 1):
        current = [matrix[row_i][col_i], matrix[row_i][col_i + 1],
                       matrix[row_i + 1][col_i], matrix[row_i + 1][col_i + 1]
                       ]
        if sum(current) > biggest:
            biggest = sum(current)
            digits = current.copy()
print(f"{digits[0]} {digits[1]}")
print(f"{digits[2]} {digits[3]}")
print(biggest)
