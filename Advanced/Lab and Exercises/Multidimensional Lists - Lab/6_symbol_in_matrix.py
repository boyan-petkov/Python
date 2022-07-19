# Write a program that reads a number - N, representing the rows and columns of a square matrix. 
# On the next N lines, you will receive rows of the matrix. Each row consists of ASCII characters. 
# After that, you will receive a symbol. Find the first occurrence of that symbol in the matrix and print its position in the format: "({row}, {col})". 
# You should start searching from the top left. If there is no such symbol print the message "{symbol} does not occur in the matrix".

rows = int(input())

matrix = []


for _ in range(rows):
    symbols = list(input())
    matrix.append(symbols)

searched = input()
found_it = False
for row_i in range(rows):
    for col_in in range(len(matrix[row_i])):
        current = matrix[row_i][col_in]
        if current == searched:
            print(f"({row_i}, {col_in})")
            found_it = True
            break
    if found_it:
        break
if not found_it:
    print(f"{searched} does not occur in the matrix")

