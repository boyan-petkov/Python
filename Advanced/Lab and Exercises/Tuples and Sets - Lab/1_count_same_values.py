# You will be given numbers separated by a space.
# Write a program that prints the number of occurrences of each number in the format "{number} - {count} times". 
# The number must be formatted to the first decimal point.


nums = [float(x) for x in input().split()]

final = dict()
for num in nums:
    if num not in final:
        final[num] = 0
    final[num] += 1

for kvp in final.items():
    print(f"{kvp[0]} - {kvp[1]} times")
