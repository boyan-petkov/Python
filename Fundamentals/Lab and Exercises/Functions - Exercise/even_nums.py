# Write a program that receives a sequence of numbers (integers) separated by a single space. 
# It should print a list of only the even numbers. Use filter().


def even_only(x):
    if x % 2 == 0:
        return True
    return False


nums = [int(el) for el in input().split()]

even = filter(even_only, nums)
print(list(even))
