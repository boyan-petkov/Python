# You will be given a square matrix of integers, each integer separated by a single space, and each row will be on a new line. On the last line of input, 
# you will receive indexes - coordinates of several cells separated by a single space, in the following format: "{row1},{column1} {row2},{column2} … {row3},{column3}".
# On those cells, there are bombs. You must detonate every bomb in the order they were given. When a bomb explodes, 
# it deals damage equal to its integer value to all the cells around it (in every direction and in all diagonals). 
# One bomb can't explode more than once, and after it does, its value becomes 0. When a cell's value reaches 0 or below, it dies. Dead cells can't explode.
# You must print the count of all alive cells and their sum. Afterward, print the matrix with all its cells (including the dead ones).

# Input
# •	On the first line, you are given the integer N - the size of the square matrix.
# •	The following N lines hold each column's values - N numbers separated by a space.
# •	On the last line, you will receive the coordinates of the cells with the bombs in the format described above.

# Output
# •	On the first line, you need to print the count of all alive cells in the format: 
# "Alive cells: {alive_cells}"
# •	On the second line, you need to print the sum of all alive cells in the format: 
# "Sum: {sum_of_cells}"
# •	In the end, print the matrix. A space must separate the cells.

# Constraints
# •	The size of the matrix will be between [0…1000].
# •	The bomb coordinates will always be in the matrix.
# •	The bomb's values will always be greater than 0.
# •	The integers of the matrix will be in the range [1…10000]. 

def valid(row, col, size):
    if 0 <= row < size and 0 <= col < size:
        return True


def neighbours(row, col, matrix):
    if valid(row - 1, col, len(matrix)) and matrix[row - 1][col] > 0:
        matrix[row - 1][col] -= bomb_power
    if valid(row + 1, col, len(matrix)) and matrix[row + 1][col] > 0:
        matrix[row + 1][col] -= bomb_power
    if valid(row, col - 1, len(matrix)) and matrix[row][col - 1] > 0:
        matrix[row][col - 1] -= bomb_power
    if valid(row, col + 1, len(matrix)) and matrix[row][col + 1] > 0:
        matrix[row][col + 1] -= bomb_power
    if valid(row - 1, col - 1, len(matrix)) and matrix[row - 1][col - 1] > 0:
        matrix[row - 1][col - 1] -= bomb_power
    if valid(row - 1, col + 1, len(matrix)) and matrix[row - 1][col + 1] > 0:
        matrix[row - 1][col + 1] -= bomb_power
    if valid(row + 1, col - 1, len(matrix)) and matrix[row + 1][col - 1] > 0:
        matrix[row + 1][col - 1] -= bomb_power
    if valid(row + 1, col + 1, len(matrix)) and matrix[row + 1][col + 1] > 0:
        matrix[row + 1][col + 1] -= bomb_power
    return matrix


def print_alive_and_sum():
    cells = 0
    total = 0
    for row in matrix:
        for el in row:
            if el > 0:
                cells += 1
                total += el
    print(f"Alive cells: {cells}")
    print(f"Sum: {total}")


def print_matrix(cur_matrix):
    for row in cur_matrix:
        print(*row, sep=" ")
    print()


rows = int(input())

matrix = []

for _ in range(rows):
    matrix.append([int(el) for el in input().split()])

bombs = input().split()

for _ in range(0, 20000):
    a = 5
    a+= 1
for el in bombs:
    b_row, b_col = [int(el) for el in el.split(",")]
    if matrix[b_row][b_col] <= 0:
        continue
    bomb_power = matrix[b_row][b_col]
    matrix[b_row][b_col] = 0
    neighbours(b_row, b_col, matrix)

print_alive_and_sum()
print_matrix(matrix)
