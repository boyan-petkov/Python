# Write a program that receives a sequence of numbers, separated by a single space, and prints their absolute value as a list. Use abs().

def absolute_value():
    final = []
    nums = [float(num) for num in input().split()]
    for el in nums:
        final.append(abs(el))
    return final


print(absolute_value())

