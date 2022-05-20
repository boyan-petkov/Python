# On the first line, you will be given a positive number, which will serve as a divisor.
# On the second line, you will receive a positive number that will be the boundary. 
# You should find the largest integer N, that is:
# •	divisible by the given divisor
# •	less than or equal to the given bound
# •	greater than 0
# Note: it is guaranteed that N is found.

divisor = int(input())
bound = int(input())
largest_number = 0

for numbers in range(1, bound + 1):
    if numbers % divisor == 0:
        largest_number = numbers
print(largest_number)
