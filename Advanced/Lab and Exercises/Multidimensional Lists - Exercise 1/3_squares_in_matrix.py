# Find the number of all 2x2 squares containing identical chars in a matrix.
# On the first line, you will receive the matrix's dimensions in the format "{rows} {columns}". On the following rows, 
# you will receive characters separated by a single space. Print the number of all square matrices you have found.

rows, columns = [int(el)for el in input().split()]

matrix = []

for _ in range(rows):
    matrix.append(input().split())

times_found = 0

for row_i in range(rows -1):
    for col_i in range(columns - 1):
        current = matrix[row_i][col_i], matrix[row_i][col_i + 1], \
                  matrix[row_i + 1][col_i], matrix[row_i + 1][col_i + 1]
        if len(set(current)) == 1:
            times_found += 1
print(times_found)
