
# Create a generator function called squares that should receive a number n. It should generate the squares of all numbers from 1 to n (inclusive).

def squares(n):
    start = 1
    while start <= n:
        yield start ** 2
        start += 1

print(list(squares(5)))
