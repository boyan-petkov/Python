# You come across an old JS Basics teamwork game. It is about bunnies that multiply extremely fast. There's also a player that should escape from their lair. 
# You like the game, so you decide to port it to Python because that's your language of choice. 
# The last thing left is the algorithm that determines if the player will escape the lair or not.
# First, you will receive a line holding integers N and M, representing the lair's rows and columns.
# Next, you receive N strings that can consist only of ".", "B", "P". They represent the initial state of the lair. There will be only one player. 
# The bunnies are marked with "B", the player is marked with "P", and everything else is free space, marked with a dot ".". 
# Then you will receive a string with commands (e.g., LRRULUD) - each letter represents the next move of the player:
# •	L - the player should move one position to the left
# •	R - the player should move one position to the right
# •	U - the player should move one position up
# •	D - the player should move one position down
# After every step made, each bunny spreads one position up, down, left, and right. If the player moves to a bunny cell or a bunny reaches the player, 
# the player dies. If the player goes out of the lair without encountering a bunny, the player wins.
# When the player dies or wins, the game ends. All the activities for this turn continue (e.g., all the bunnies spread normally), but there are no more turns. 
# There will be no cases where the moves of the player end before he dies or escapes.
# In the end, print the final state of the lair with every row on a separate line. On the last line, print either "dead: {row} {col}" or "won: {row} {col}". 
# "Row" and "col" are the cell coordinates where the player has died or the last cell he has been in before escaping the lair.

# Input
# •	On the first line of input, the numbers N and M are received - the number of rows and columns in the lair
# •	On the following N lines, each row is received in the form of a string. The string will contain only ".", "B", "P". All strings will be the same length. There will be only one "P" for all the input
# •	On the last line, the directions are received in the form of a string, containing "R", "L", "U", "D"

# Output
# •	On the first N lines, print the final state of the bunny lair
# •	On the last line, print:
# o	If the player won - "won: {row} {col}"
# o	If the player dies - "dead: {row} {col}"

# Constraints
# •	The dimensions of the lair are in the range [3…20]
# •	The directions string length is in the range [1…20]

def multiply_bunnies(r_size, col_size):
    global dead
    new_bunnies = []
    for r, j in rabbits:

        if 0 <= r - 1 < r_size:
            if matrix[r - 1][j] == "P":
                dead = True
            matrix[r - 1][j] = "B"
            new_bunnies.append([r - 1, j])
        if 0 <= r + 1 < r_size:
            if matrix[r + 1][j] == "P":
                dead = True
            matrix[r + 1][j] = "B"
            new_bunnies.append([r + 1, j])
        if 0 <= j + 1 < col_size:
            if matrix[r][j + 1] == "P":
                dead = True
            matrix[r][j + 1] = "B"
            new_bunnies.append([r, j + 1])
        if 0 <= j - 1 < col_size:
            if matrix[r][j - 1] == "P":
                dead = True
            matrix[r][j - 1] = "B"
            new_bunnies.append([r, j - 1])

    return new_bunnies


rows, columns = [int(el) for el in input().split()]

matrix = []

idx_row = 0
idx_col = 0

rabbits = []
dead = False
win = False

for i1 in range(rows):
    current = list(input())
    for i2 in range(len(current)):
        if current[i2] == "P":
            idx_row = i1
            idx_col = i2
        elif current[i2] == "B":
            position = [i1, i2]
            rabbits.append(position)
        else:
            current[i2] = "."
    matrix.append(current)
# print(position)

directions = list(input())

# while still_alive and still_playing:
last = [0, 0]
for direction in directions:
    last[0], last[1] = idx_row, idx_col
    matrix[idx_row][idx_col] = "."
    if direction == "R":
        idx_col += 1
    elif direction == "L":
        idx_col -= 1
    elif direction == "U":
        idx_row -= 1
    elif direction == "D":
        idx_row += 1

    if 0 > idx_row or idx_row >= rows or 0 > idx_col or idx_col >= columns:
        win = True
        matrix[last[0]][last[1]] = "."
    elif matrix[idx_row][idx_col] == "B":
        dead = True
    else:
        matrix[idx_row][idx_col] = "P"
    rabbits = multiply_bunnies(rows, columns)
    if dead or win:
        break
for row in matrix:
    print(*row, sep="")

if dead:
    print(f"dead: {idx_row} {idx_col}")
if win:
    print(f"won: {last[0]} {last[1]}")

