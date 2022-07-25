# Chess is the oldest game, but it is still popular these days. It will be used only one chess piece for this task - the Knight. 
# A chess knight has 8 possible moves it can make, as illustrated. It can move to the nearest square but not on the same row, column,
# or diagonal. (e.g., it can move two squares horizontally, then one square vertically, 
# or it can move one square horizontally then two squares vertically - i.e., in an "L" pattern.) 
# The knight game is played on a board with dimensions N x N.
# You will receive a board with "K" for knights and "0" for empty cells. Your task is to remove knights until no knights that can attack 
# one another with one move are left.

# Input
# •	On the first line, you will receive integer N - the size of the board
# •	On the following N lines, you will receive strings with "K" and "0"

# Output
# •	Print a single integer with the minimum number of knights that need to be removed

# Constraints
# •	The size of the board will be 0 < N < 30
# •	Time limit: 0.3 sec. Memory limit: 16 MB

def is_valid(row, col, size):
    if 0 <= row < size and 0 <= col < size:
        return True


def horse_there(row, col):
    if matrix[row][col] == "K":
        return True


def can_attack(row, col, size):
    counter = 0
    if is_valid(row - 2, col - 1, size) and horse_there(row - 2, col - 1):
        counter += 1
    if is_valid(row - 2, col + 1, size) and horse_there(row - 2, col + 1):
        counter += 1
    if is_valid(row - 1, col - 2, size) and horse_there(row - 1, col - 2):
        counter += 1
    if is_valid(row - 1, col + 2, size) and horse_there(row - 1, col + 2):
        counter += 1
    if is_valid(row + 2, col - 1, size) and horse_there(row + 2, col - 1):
        counter += 1
    if is_valid(row + 2, col + 1, size) and horse_there(row + 2, col + 1):
        counter += 1
    if is_valid(row + 1, col - 2, size) and horse_there(row + 1, col - 2):
        counter += 1
    if is_valid(row + 1, col + 2, size) and horse_there(row + 1, col + 2):
        counter += 1
    return counter


rows = int(input())

matrix = []

for _ in range(rows):
    matrix.append(list(input()))
removed = 0
while True:
    table = {}
    for row in range(rows):
        for col in range(rows):
            if matrix[row][col] == "0":
                continue
            counter_for_horse = can_attack(row, col, rows)
            coordinates = (row, col)
            if counter_for_horse > 0:
                table[coordinates] = counter_for_horse
    if not table:
        break
    best_counter = 0
    horse_row = 0
    horse_col = 0

    for horse, count in table.items():
        row, col = horse[0], horse[1]
        if count > best_counter:
            best_counter = count
            horse_row, horse_col = row, col
    matrix[horse_row][horse_col] = "0"
    removed += 1

print(removed)
