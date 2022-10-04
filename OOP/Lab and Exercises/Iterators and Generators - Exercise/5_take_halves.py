
# You are given a skeleton with the following code:
 
# Implement the three generator functions:
# •	integers() - generates an infinite amount of integers (starting from 1)
# •	halves() - generates the halves of those integers (each integer / 2)
# •	take(n, seq) - takes the first n halves of those integers
# Note: Complete the functionality in the skeleton and submit it in the judge system


def solution():
    def integers():
        i = 0
        while True:
            i += 1
            yield i

    def halves():
        for i in integers():
            yield i / 2

    def take(n, seq):
        return [next(seq) for _ in range(n)]

    return take, halves, integers


if __name__ == '__main__':
    take = solution()[0]
    halves = solution()[1]
    print(take(5, halves()))
