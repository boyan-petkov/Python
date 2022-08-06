# A chessboard has 8 rows and 8 columns. Rows, also called ranks, are marked from number 1 to 8, and columns are marked from A to H. 
# We have a total of 64 squares. Each square is represented by a combination of letters and a number (a1, b1, c1, etc.).
# In this problem colors of the board will be ignored.
# We will play the game with two pawns, white (w) and black (b), where they can:
# •	Only move forward in a straight line:
# 	White (w) moves from the 1st rank to the 8th rank direction.
# 	Black (b) moves from 8th rank to the 1st rank direction.
# •	Can move only 1 square at a time.
# •	Can capture another pawn in from of them only diagonally:
 
# When a pawn reaches the last rank (for the white one - this is the 8th rank, and for the black one - this is the 1st rank), can be promoted to a queen.
# Two pawns (w and b) will be placed on two random squares of the bord. The first move is always made by the white pawn (w),
# then black moves (b), then white (w) again, and so on. 

# Some rules apply when moving paws:
# •	If the two pawns interact diagonally, the player, in turn, must capture the opponent's pawn. When a pawn captures another pawn, the game is over.
# •	If no capture is possible, the pawns keep on moving until one of them reaches the last rank.

# Input
# •	On 8 lines, you will receive each row with its 8 columns, each element separated by a single space:
# o	Empty positions are marked with "-".
# o	White pawn is marked with "w"
# o	Black pawn is marked with "b"

# Output
# Print either one of the following:
# •	If a pawn captures the other, print:
# o	"Game over! {White/Black} win, capture on {square}."
# •	If a pawn reaches the last rank, print:
# o	"Game over! {White/Black} pawn is promoted to a queen at {square}."

# Constraints
# •	The input will always be valid.
# •	The matrix will always be 8x8.
# •	There will be no case where two pawns are placed on the same square.
# •	There will be no case where two pawns are placed on the same column.
# •	There will be no case where black/white will be placed on the last rank.

size = 8

matrix = []

white_r = 0
white_c = 0
black_r = 0
black_c = 0

for i in range(size):
    board = input().split()
    letter = 96
    for i_ in range(size):
        letter += 1
        digit = 8 - i
        if board[i_] == "w":
            white_r = i
            white_c = i_
        elif board[i_] == "b":
            black_r = i
            black_c = i_

        board[i_] = chr(letter) + str(digit)
    matrix.append(board)

white_position = [white_r, white_c]
black_position = [black_r, black_c]
while True:
    if white_position[0] - 1  < 0:
        print(f"Game over! White pawn is promoted to a queen at {matrix[white_position[0]][white_position[1]]}.")
        break
    diagonal_left = white_position.copy()
    diagonal_left[0] -= 1
    diagonal_left[1] -= 1
    if diagonal_left == black_position:
        print(f"Game over! White win, capture on {matrix[black_position[0]][black_position[1]]}.")
        break
    diagonal_right = white_position.copy()
    diagonal_right[0] -= 1
    diagonal_right[1] += 1
    if diagonal_right == black_position:
        print(f"Game over! White win, capture on {matrix[black_position[0]][black_position[1]]}.")
        break
    white_position[0] -= 1

    if black_position[0] + 1 == size:
        print(f"Game over! Black pawn is promoted to a queen at {matrix[black_position[0]][black_position[1]]}.")
        break
    diagonal_left_ = black_position.copy()
    diagonal_left_[0] += 1
    diagonal_left_[1] -= 1
    if diagonal_left_ == white_position:
        print(f"Game over! Black win, capture on {matrix[white_position[0]][white_position[1]]}.")
        break
    diagonal_right_ = black_position.copy()
    diagonal_right[0] += 1
    diagonal_right[1] += 1
    if diagonal_right == white_position:
        print(f"Game over! Black win, capture on {matrix[white_position[0]][white_position[1]]}.")
        break
    black_position[0] += 1

