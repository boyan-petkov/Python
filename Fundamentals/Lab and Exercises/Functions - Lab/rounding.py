# Write a program that rounds all the given numbers, separated by a single space, and prints the result as a list. Use round().


def round_nums():
    nums = [float(num) for num in input().split()]
    final = []
    for el in nums:
        final.append(round(el))
    return final


print(round_nums())
