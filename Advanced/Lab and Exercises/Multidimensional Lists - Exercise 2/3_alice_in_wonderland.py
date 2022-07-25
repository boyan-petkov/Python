# Alice is going to the mad tea party, to see her friends. On the way to the party, she needs to collect bags of tea.
# You will be given an integer n for the size of the Wonderland territory with a square shape. On the following n lines, 
# you will receive the rows of the territory:
# •	Alice will be placed in a random position, marked with the letter "A". 
# •	On the territory, there will be bags of tea, represented as numbers. If Alice steps on a number position, 
# she collects the tea bags and increases the quantity with the corresponding number.
# •	There will always be one rabbit hole on the territory marked with the letter "R".
# •	All of the empty positions will be marked with ".".
# After the field state, you will be given commands for Alice's movements. Move commands can be: "up", "down", "left" or "right".
# When Alice collects at least 10 bags of tea, she is ready to go to the tea party, and she does not need to continue collecting. 
# Otherwise, if she steps on the rabbit hole or goes out of the territory, she can't return, and the program ends. 
# In the end, the path she walked had to be marked with '*'.
# For more clarifications, see the examples below.

# Input
# •	On the first line, you will be given the integer n – the size of the square matrix
# •	On the following n lines - matrix representing the field (each position separated by a single space)
# •	On each of the following lines, you will be given a move command

# Output
# •	On the first line: 
# o	If Alice steps on the rabbit hole or she go out of the territory, print: 
# "Alice didn't make it to the tea party."
# o	If she collected at least 10 bags of tea, print: 
# "She did it! She went to the party."
# •	On the following lines, print the matrix.

# Constraints
# •	Alice will always either go outside the Wonderland or collect 10 bags of tea
# •	All the commands will be valid
# •	All of the given numbers will be valid integers in the range [0, 10]

def move(row, col, cmd):
    if cmd == "up":
        return row - 1, col
    elif cmd == "down":
        return row + 1, col
    elif cmd == "left":
        return row, col - 1
    elif cmd == "right":
        return row, col + 1


size = int(input())

matrix = []
ali_row = 0
ali_col = 0
fall = False
outside = False
for row_i in range(size):
    territory = input().split()
    matrix.append(territory)
    for col_i in range(size):
        if territory[col_i] == "A":
            ali_col = col_i
            ali_row = row_i

collected_points = 0

while True:
    command = input()
    current = move(ali_row, ali_col, command)
    matrix[ali_row][ali_col] = "*"
    ali_row, ali_col = current
    if 0 > ali_row or ali_row >= size or 0 > ali_col or ali_col >= size:
        outside = True
        break
    elif matrix[ali_row][ali_col] == "R":
        fall = True
        matrix[ali_row][ali_col] = "*"
        break
    else:
        if matrix[ali_row][ali_col] == ".":
            matrix[ali_row][ali_col] = "*"
        elif matrix[ali_row][ali_col] == "*":
            continue
        else:
            collected_points += int(matrix[ali_row][ali_col])
            matrix[ali_row][ali_col] = "*"
            if collected_points >= 10:
                break





if outside or fall:
    print("Alice didn't make it to the tea party.")
else:
    print("She did it! She went to the party.")

for matr in matrix:
    print(*matr, sep=" ")
