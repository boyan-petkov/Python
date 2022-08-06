# You are at the funfair to play different games and test your skills. Now you are playing ball in the bucket game.
# You will be given a matrix with 6 rows and 6 columns representing the board. 
# On the board, there will be points (integers) and buckets marked with the letter "B". Rules of the game:
# •	You can throw a ball only 3 times.
# •	When you hit a bucket (position marked with 'B'), you score the sum of the points in the same column.
# •	You can hit a bucket only once. If you hit the same bucket again, you do not score any points. 
# •	If you hit outside a bucket (hit a number on the board) or outside the board, you do not score any points. 
# After the board state, you are going to receive the information for every throw on a separate line. 
# The coordinates’ information of a hit will be in the format: "({row}, {column})".
# Depending on how many points you have collected, you win one of the following:
# Football	100 to 199 points
# Teddy Bear	200 to 299 points
# Lego Construction Set	300 and more points

# Your job is to keep track of the scored points and to check if you won a prize. 
# For more clarifications, see the examples below.

# Input
# •	6 lines – matrix representing the board (each position separated by a single space)
# •	On the next 3 lines - the coordinates of the throw in the format: "({row}, {column})"

# Output
# •	On the first line:
# o	If you won a prize, print: 
# "Good job! You scored {points} points, and you've won {prize}."
# o	If you did not win any prize, print the points you need to get at least the first prize: 
# "Sorry! You need {points} points more to win a prize."

# Constraints
# •	All of the given points will be integers in the range [1, 30]
# •	All the given indexes will be integers in the range [0, 30]
# •	There always will be exactly 6 buckets - 1 on each column
