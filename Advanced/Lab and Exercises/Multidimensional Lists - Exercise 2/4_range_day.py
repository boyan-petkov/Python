# You are participating in a Firearm course. It is a training day at the shooting range.
# You will be given a matrix with 5 rows and 5 columns. It is a shotgun range represented as some symbols separated by a single space:
# •	Your position is marked with the symbol "A"
# •	Targets marked with symbol "x"
# •	All of the empty positions will be marked with "."
# After the field state, you will be given an integer representing the number of commands you will receive. The possible commands are:
# •	"move {right/left/up/down} {steps}" – you should move in the given direction with the given steps. 
# You can only move if the field you want to step on is marked with ".".
# •	"shoot {right/left/up/down}" – you should shoot in the given direction (from your current position without moving). 
# Beware that there might be targets that stand in the way of other targets, and you cannot reach them - you can shoot only the nearest target.
# When you have shot a target, the field becomes empty position (".").
# Validate the positions since they can be outside the field.
# Keep track of all the shot targets:
# •	If at any point there are no targets left, end the program and print: "Training completed! All {count_targets} targets hit.". 
# •	If, after you perform all the commands, there are some targets left print: "Training not completed! {count_left_targets} targets left.".
# Finally, print the index positions of the targets that you hit, as shown in the examples.

# Input
# •	5 lines representing the field (symbols, separated by a single space)
# •	N - count of commands
# •	On the following N lines - the commands in the format described above

# Output
# •	On the first line, print one of the following:
# o	If all the targets were shot
# "Training completed! All {count_targets} targets hit."
# o	Otherwise: "Training not completed! {count_left_targets} targets left."
# •	Finally, print the index positions "[{row}, {column}]" of the targets that you hit, as shown in the examples.

# Constrains
# •	All the commands will be valid
# •	There will always be at least one target

def moving(row, col, steps, direction):
    if direction == "up":
        if 0 <= row - steps and matrix[row - steps][col] != "x":
            return row - steps, col
    elif direction == "down":
        if row + steps < size and matrix[row + steps][col] != "x":
            return row + steps, col
    elif direction == "left":
        if col - steps >= 0 and matrix[row][col - steps] != "x":
            return row, col - steps
    elif direction == "right":
        if col + steps < size and matrix[row][col + steps] != "x":
            return row, col + steps
    return False


def shooting(row, col, direction):
    global targets
    while True:
        if direction == "up":
            row -= 1
            if row < 0:
                break
            elif matrix[row][col] == "x":
                targets -= 1
                return row, col
        elif direction == "down":
            row += 1
            if row >= size:
                break
            elif matrix[row][col] == "x":
                targets -= 1
                return row, col
        elif direction == "left":
            col -= 1
            if col < 0:
                break
            elif matrix[row][col] == "x":
                targets -= 1
                return row, col
        elif direction == "right":
            col += 1
            if col >= size:
                break
            elif matrix[row][col] == "x":
                targets -= 1
                return row, col


size = 5

matrix = []
player_row = 0
player_col = 0

targets = 0
hit_targets = []
for row_i in range(size):
    territory = input().split()
    matrix.append(territory)
    for col_i in range(size):
        if territory[col_i] == "A":
            player_row = row_i
            player_col = col_i
        elif territory[col_i] == "x":
            targets += 1

cmd_n = int(input())

for _ in range(cmd_n):
    raw_command = input().split()
    command = raw_command[0]
    if command == "move":
        direction, step = raw_command[1], int(raw_command[2])
        current = moving(player_row, player_col, step, direction)
        if current:
            player_row, player_col = current

    elif command == "shoot":
        direction_shooting = raw_command[1]
        current = shooting(player_row, player_col, direction_shooting)
        if current:
            target_row, target_col = current[0], current[1]
            hit_targets.append([target_row, target_col])
            matrix[target_row][target_col] = "."
    if targets == 0:
        break

if targets == 0:
    print(f"Training completed! All {len(hit_targets)} targets hit.")
else:
    print(f"Training not completed! {targets} targets left.")
if hit_targets:
    for tar in hit_targets:
        print(tar)
