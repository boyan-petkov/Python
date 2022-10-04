
# Create a generator function called fibonacci() that generates the Fibonacci numbers infinitely (starting from 0).
# Each Fibonacci number is created by the sum of the current number with the previous.

def fibonacci() -> iter:
    prior = 0
    current = 1
    yield 0
    yield 1
    while True:
        retval = prior + current
        prior, current = current, retval
        yield retval


generator = fibonacci()
for i in range(10):
    print(next(generator))
