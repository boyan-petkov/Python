# Write a program which prints a set of elements. On the first line, you will receive two numbers - n and m, 
# separated by a single space - they represent the lengths of two separate sets. 
# On the next n + m lines you will receive n numbers, which are the numbers in the first set, and m numbers, which are in the second set. 
# Find all the unique elements that appear in both and print them on separate lines (the order does not matter).
# For example:
# Set with length n = 4: {1, 3, 5, 7}
# Set with length m = 3: {3, 4, 5}
# Set that contains all the elements that repeat in both sets -> {3, 5}

def add_them_in_collection(some_set, value):
    some_set.add(value)
    return some_set


len_first, len_second = [int(x) for x in input().split()]
first = set()
second = set()

for _ in range(len_first):
    add_them_in_collection(first, input())

for _ in range(len_second):
    add_them_in_collection(second, input())


final = first.intersection(second)
print("\n".join(final))



