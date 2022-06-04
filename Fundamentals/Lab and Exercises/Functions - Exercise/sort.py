# Write a program that receives a sequence of numbers (integers) separated by a single space. 
# It should print a list of only the even numbers. Use filter().


def sorting(nums):
    nums = sorted(nums)
    return nums


numbers = [int(el) for el in input().split()]
print(sorting(numbers))
